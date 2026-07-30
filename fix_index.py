import os
import json
from bs4 import BeautifulSoup
import datetime

main_files = [
    'index.html',
    'portfolio.html',
    'quem-somos.html',
    'solucoes.html',
    'contato.html',
    'eventos.html',
    'solucoes/manual-do-verdadeiro-papai-noel.html',
    'trabalhe-conosco.html'
]

orphan_files = [
    'design_system1.html',
    'header_standard.html',
    'missing_footer.html',
    'new_segment.html',
    'scratch_evt.html',
    'scratch_idx.html',
    'scratch_trabalhe_conosco_cta.html'
]

base_url = "https://cria-a-o-site-noel.vercel.app"

# 1. Update Canonical and OG URL
for filepath in main_files:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    head = soup.head
    if not head:
        continue
        
    # Clean URL path
    clean_path = filepath.replace('.html', '')
    if clean_path == 'index':
        clean_path = ''
    else:
        clean_path = '/' + clean_path
        
    clean_url = base_url + clean_path
    
    # Update canonical
    canon = head.find('link', rel='canonical')
    if canon:
        canon['href'] = clean_url
        
    # Update og:url
    og_url = head.find('meta', attrs={'property': 'og:url'})
    if og_url:
        og_url['content'] = clean_url
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"Fixed clean URL for {filepath}")

# 2. Add noindex to orphan files
for filepath in orphan_files:
    if not os.path.exists(filepath):
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
            
    soup = BeautifulSoup(content, 'html.parser')
        
    head = soup.head
    if not head:
        head = soup.new_tag('head')
        if soup.html:
            soup.html.insert(0, head)
        else:
            soup.insert(0, head)
        
    robots = head.find('meta', attrs={'name': 'robots'})
    if robots:
        robots['content'] = 'noindex,nofollow'
    else:
        head.append(soup.new_tag('meta', attrs={'name': 'robots', 'content': 'noindex,nofollow'}))
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"Added noindex to {filepath}")

# 3. Create sitemap.xml
sitemap_xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
today = datetime.datetime.now().strftime("%Y-%m-%d")

for filepath in main_files:
    clean_path = filepath.replace('.html', '')
    if clean_path == 'index':
        clean_path = ''
    else:
        clean_path = '/' + clean_path
        
    clean_url = base_url + clean_path
    priority = "1.0" if clean_path == "" else "0.8"
    
    sitemap_xml += f"""  <url>
    <loc>{clean_url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>\n"""

sitemap_xml += "</urlset>\n"

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)
    
print("Updated sitemap.xml")

# 4. Create 404.html
if os.path.exists('index.html'):
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # Extract head
    head_content = str(soup.head) if soup.head else "<head><title>Página não encontrada</title></head>"
    
    html_404 = f"""<!DOCTYPE html>
<html lang="pt-BR">
{head_content}
<body style="display:flex; justify-content:center; align-items:center; height:100vh; text-align:center; font-family:sans-serif; background-color:#f5f5f5; color:#333; margin:0;">
    <div>
        <h1 style="font-size: 4rem; margin-bottom: 10px;">404</h1>
        <p style="font-size: 1.5rem; margin-bottom: 20px;">Página não encontrada</p>
        <a href="/" style="text-decoration:none; padding: 10px 20px; background-color: #d11212; color: white; border-radius: 5px; font-weight: bold;">Voltar para o Início</a>
    </div>
</body>
</html>
"""
    with open('404.html', 'w', encoding='utf-8') as f:
        f.write(html_404)
        
    print("Created 404.html")
