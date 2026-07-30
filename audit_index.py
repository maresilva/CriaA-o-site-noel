import os
import json
from bs4 import BeautifulSoup
import glob

def audit_index():
    report = {
        'robots.txt': os.path.exists('robots.txt'),
        'sitemap.xml': os.path.exists('sitemap.xml'),
        '404.html': os.path.exists('404.html'),
        'vercel.json': os.path.exists('vercel.json'),
        'netlify.toml': os.path.exists('netlify.toml'),
        'html_files': [],
        'links_found': set(),
        'canonicals': {},
        'noindex': {},
        'pagination': {}
    }

    html_files = glob.glob('*.html') + glob.glob('*/*.html')
    # Filter out weird dirs if any, just keep the main ones
    html_files = [f for f in html_files if not f.startswith('assets\\') and not f.startswith('.git\\') and 'google' not in f]
    report['html_files'] = [f.replace('\\', '/') for f in html_files]

    for file in report['html_files']:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                
                # Extract all links
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    # Normalize href
                    href = href.split('#')[0].split('?')[0] # remove hash and query
                    if href and not href.startswith('http') and not href.startswith('mailto:') and not href.startswith('tel:'):
                        report['links_found'].add(href.lstrip('/'))
                        
                # Extract canonical
                canon = soup.find('link', rel='canonical')
                if canon:
                    report['canonicals'][file] = canon.get('href')
                    
                # Extract robots
                robots = soup.find('meta', attrs={'name': 'robots'})
                if robots and 'noindex' in robots.get('content', '').lower():
                    report['noindex'][file] = True
                    
                # Extract pagination
                prev = soup.find('link', rel='prev')
                nxt = soup.find('link', rel='next')
                if prev or nxt:
                    report['pagination'][file] = {'prev': prev.get('href') if prev else None, 'next': nxt.get('href') if nxt else None}
        except Exception as e:
            pass

    report['links_found'] = list(report['links_found'])
    
    with open('index_audit_results.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

audit_index()
print("Index audit complete.")
