import os
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

preconnects = [
    '<link href="https://www.googletagmanager.com" rel="preconnect"/>',
    '<link href="https://www.google-analytics.com" rel="preconnect"/>'
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
    
    if soup.head:
        # 1. Add defer to render blocking scripts
        for script in soup.head.find_all('script', src=True):
            if 'googletagmanager' not in script['src']:
                if not script.get('defer') and not script.get('async'):
                    script['defer'] = 'defer'
                    modified = True
                    
        # 2. Add preconnects if not present
        head_str = str(soup.head)
        for pc in preconnects:
            if 'www.googletagmanager.com' in pc and 'href="https://www.googletagmanager.com"' not in head_str:
                new_tag = soup.new_tag('link', rel='preconnect', href='https://www.googletagmanager.com')
                soup.head.insert(0, new_tag)
                modified = True
            if 'www.google-analytics.com' in pc and 'href="https://www.google-analytics.com"' not in head_str:
                new_tag = soup.new_tag('link', rel='preconnect', href='https://www.google-analytics.com')
                soup.head.insert(0, new_tag)
                modified = True
                
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Applied perf optimizations to {filepath}")

print("Perf optimization complete.")
