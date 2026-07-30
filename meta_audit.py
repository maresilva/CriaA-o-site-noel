import os
import json
from bs4 import BeautifulSoup

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

def get_meta_info(soup):
    info = {
        'title': [],
        'description': [],
        'canonical': [],
        'robots': [],
        'viewport': [],
        'charset': [],
        'language': soup.html.get('lang', None) if soup.html else None,
        'author': [],
        'og': {},
        'twitter': {}
    }
    
    # Title
    titles = soup.find_all('title')
    info['title'] = [t.get_text(strip=True) for t in titles]
    
    # Canonical
    canonicals = soup.find_all('link', rel='canonical')
    info['canonical'] = [c.get('href') for c in canonicals]
    
    # Metas
    for meta in soup.find_all('meta'):
        # Charset
        if meta.get('charset'):
            info['charset'].append(meta.get('charset'))
            
        name = meta.get('name', '').lower()
        property = meta.get('property', '').lower()
        content = meta.get('content', '')
        
        if name == 'description':
            info['description'].append(content)
        elif name == 'robots':
            info['robots'].append(content)
        elif name == 'viewport':
            info['viewport'].append(content)
        elif name == 'author':
            info['author'].append(content)
        elif property.startswith('og:'):
            info['og'][property] = info['og'].get(property, []) + [content]
        elif name.startswith('twitter:'):
            info['twitter'][name] = info['twitter'].get(name, []) + [content]
            
    return info

for file in files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    report[file] = get_meta_info(soup)

with open('meta_report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2)

print("Meta audit complete.")
