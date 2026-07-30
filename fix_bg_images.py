import os
import re

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

pattern = re.compile(r"(background(?:-image)?:\s*url\([^)]+)\.(png|jpg|jpeg)([^)]*\))", re.IGNORECASE)

for filepath in files:
    if not os.path.exists(filepath):
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
            
    new_content, count = pattern.subn(r"\1.webp\3", content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {count} background images in {filepath}")

print("Background image fix complete.")
