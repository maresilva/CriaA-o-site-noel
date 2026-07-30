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

for filepath in files:
    if not os.path.exists(filepath):
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
            
    # Fix missed inline urls inside gradients or anything else
    # Finds url(...) where it ends in png, jpg, jpeg
    def replacer(match):
        return f"url('{match.group(1)}.webp')"
        
    content = re.sub(r"url\(['\"]?(.*?)(\.png|\.jpg|\.jpeg)['\"]?\)", replacer, content, flags=re.IGNORECASE)
    
    # Fix the encoding bug for that specific image
    content = content.replace('background-segunda-sesso-shopping-decorado', 'background-segunda-sessão-shopping-decorado')
    content = content.replace('background-segunda-sesso-shopping-decorado', 'background-segunda-sessão-shopping-decorado')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Robuster bg fix complete.")
