import os

old_domain = "https://cria-a-o-site-noel.vercel.app"
new_domain = "https://criaacao.com"

files_to_update = [
    'sitemap.xml',
    'robots.txt',
    'index.html',
    'portfolio.html',
    'quem-somos.html',
    'solucoes.html',
    'contato.html',
    'eventos.html',
    'trabalhe-conosco.html',
    'solucoes/manual-do-verdadeiro-papai-noel.html',
    '404.html'
]

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
            
    if old_domain in content:
        content = content.replace(old_domain, new_domain)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated domain in {filepath}")

print("Domain fix complete.")
