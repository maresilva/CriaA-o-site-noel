import os
import datetime
import glob
import re

# 1. Update sitemap.xml
urls = [
    'https://www.criaacao.com',
    'https://www.criaacao.com/portfolio',
    'https://www.criaacao.com/quem-somos',
    'https://www.criaacao.com/solucoes',
    'https://www.criaacao.com/contato',
    'https://www.criaacao.com/eventos',
    'https://www.criaacao.com/trabalhe-conosco',
    'https://www.criaacao.com/solucoes/manual-do-verdadeiro-papai-noel',
    'https://www.criaacao.com/solucoes/shopping-centers',
    'https://www.criaacao.com/solucoes/gestao-publica',
    'https://www.criaacao.com/solucoes/escolas',
    'https://www.criaacao.com/solucoes/empresas-e-corporativo',
    'https://www.criaacao.com/solucoes/condominios-e-residencias',
    'https://www.criaacao.com/solucoes/buffets-e-espacos-de-eventos',
    'https://www.criaacao.com/solucoes/hospitais',
    'https://www.criaacao.com/solucoes/creches',
    'https://www.criaacao.com/solucoes/instituicoes-de-acolhimento'
]

today = datetime.datetime.now().strftime('%Y-%m-%d')

xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    priority = '1.0' if url == 'https://www.criaacao.com' else '0.8'
    xml_content += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>{priority}</priority>\n  </url>\n'
xml_content += '</urlset>\n'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(xml_content)

print('Updated sitemap.xml to WWW.')

# 2. Update HTML Canonical and Open Graph Tags
html_files = glob.glob('*.html') + glob.glob('solucoes/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace exactly "https://criaacao.com/" with "https://www.criaacao.com/"
    # specifically inside canonical href and og:url content, and og:image, twitter:image
    
    # We can just safely replace it globally since we are just adding 'www.' to our own domain.
    # However, to be safe, let's only replace it where it follows href=" or content="
    content = re.sub(r'href="https://criaacao\.com(.*?)"', r'href="https://www.criaacao.com\1"', content)
    content = re.sub(r'content="https://criaacao\.com(.*?)"', r'content="https://www.criaacao.com\1"', content)

    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.write(content)

print(f'Updated canonicals in {len(html_files)} HTML files.')

# 3. Update robots.txt
robots_content = """User-agent: *
Allow: /
Sitemap: https://www.criaacao.com/sitemap.xml
"""
with open('robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_content)

print('Updated robots.txt.')
