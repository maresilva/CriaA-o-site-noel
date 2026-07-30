import os
import re
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

for filepath in files:
    if not os.path.exists(filepath):
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
            
    soup = BeautifulSoup(content, 'html.parser')
    modified = False
    
    # 1. Fix viewport
    viewport = soup.find('meta', attrs={'name': 'viewport'})
    if viewport:
        content_val = viewport.get('content', '')
        if 'maximum-scale' in content_val or 'user-scalable' in content_val:
            # Clean it to just width=device-width, initial-scale=1
            viewport['content'] = 'width=device-width, initial-scale=1'
            modified = True
            
    # 2. Inject mobile-seo.css
    css_path = 'assets/css/mobile-seo.css'
    if filepath.startswith('solucoes/'):
        css_path = '../' + css_path
        
    head_str = str(soup.head) if soup.head else ''
    if 'mobile-seo.css' not in head_str and soup.head:
        new_link = soup.new_tag('link', rel='stylesheet', href=css_path)
        soup.head.append(new_link)
        modified = True
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Fixed mobile SEO in {filepath}")

print("Mobile SEO fix complete.")
