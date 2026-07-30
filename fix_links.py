import os
from bs4 import BeautifulSoup
import urllib.parse

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

def fix_links(filepath):
    if not os.path.exists(filepath):
        return
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
            
    soup = BeautifulSoup(content, 'html.parser')
    
    modified = False
    
    for a in soup.find_all('a', href=True):
        href = a['href']
        
        # Ignore externals, mailto, tel, anchors
        if href.startswith('http') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('#'):
            continue
            
        # Parse link
        parsed = urllib.parse.urlsplit(href)
        path = parsed.path
        
        # Clean relative paths
        path = path.lstrip('/')
        path = path.replace('../', '')
        path = path.replace('./', '')
        
        # Map to root absolute clean path
        new_path = path
        if path == 'index.html' or path == 'index' or path == '':
            new_path = '/'
        elif path == 'manual-do-verdadeiro-papai-noel.html' or path == 'solucoes/manual-do-verdadeiro-papai-noel.html':
            new_path = '/solucoes/manual-do-verdadeiro-papai-noel'
        elif path.endswith('.html'):
            new_path = '/' + path.replace('.html', '')
        elif not path.startswith('/'):
            new_path = '/' + path
            
        # Reconstruct href with query and hash
        new_href = new_path
        if parsed.query:
            new_href += '?' + parsed.query
        if parsed.fragment:
            new_href += '#' + parsed.fragment
            
        if new_href != href:
            a['href'] = new_href
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Fixed links in {filepath}")

for f in files:
    fix_links(f)

print("Link fixing complete.")
