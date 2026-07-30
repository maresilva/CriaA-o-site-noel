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
    
    # Find all logos
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if 'logo' in src.lower():
            # If it has max-height but not width: auto, it stretches
            style = img.get('style', '')
            if 'max-height' in style and 'width: auto' not in style:
                img['style'] = style + '; width: auto;'
                modified = True
                
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Fixed logo in {filepath}")

print("Logo fix complete.")
