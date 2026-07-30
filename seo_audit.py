import os
from bs4 import BeautifulSoup
import json

files = [
    'index.html',
    'portfolio.html',
    'quem-somos.html',
    'solucoes.html',
    'contato.html',
    'eventos.html',
    'solucoes/manual-do-verdadeiro-papai-noel.html',
    'trabalhe-conosco.html'
]

report = {}

def get_headings(soup):
    headings = []
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        headings.append({
            'tag': tag.name,
            'text': tag.get_text(strip=True)[:30]
        })
    return headings

def get_landmarks(soup):
    return {
        'header': len(soup.find_all('header')),
        'nav': len(soup.find_all('nav')),
        'main': len(soup.find_all('main')),
        'footer': len(soup.find_all('footer')),
        'section': len(soup.find_all('section')),
        'article': len(soup.find_all('article')),
        'aside': len(soup.find_all('aside')),
    }

def get_a11y_issues(soup):
    issues = []
    
    # Missing aria-label on empty links
    for a in soup.find_all('a'):
        if not a.get_text(strip=True) and not a.find(['img', 'svg']) and not a.get('aria-label'):
            issues.append(f"Empty link without aria-label (href: {a.get('href', '#')})")
        if a.find('svg') and not a.get_text(strip=True) and not a.get('aria-label') and not a.get('title'):
            issues.append(f"Icon link (SVG) without aria-label (href: {a.get('href', '#')})")

    # Inputs without labels or aria-labels
    for input_tag in soup.find_all(['input', 'textarea', 'select']):
        if input_tag.get('type') in ['hidden', 'submit', 'button']:
            continue
        
        has_id = input_tag.get('id')
        has_aria = input_tag.get('aria-label')
        has_label = False
        
        if has_id:
            label = soup.find('label', attrs={'for': has_id})
            if label:
                has_label = True
                
        parent_label = input_tag.find_parent('label')
        if parent_label:
            has_label = True
            
        if not has_label and not has_aria:
            name = input_tag.get('name', 'unknown')
            issues.append(f"Input/Textarea '{name}' missing label and aria-label")

    return issues

for file in files:
    if not os.path.exists(file):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    headings = get_headings(soup)
    h1_count = sum(1 for h in headings if h['tag'] == 'h1')
    
    report[file] = {
        'h1_count': h1_count,
        'headings': headings,
        'landmarks': get_landmarks(soup),
        'a11y_issues': get_a11y_issues(soup)
    }

with open('seo_report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2)

print("Report generated in seo_report.json")
