import datetime

urls = [
    'https://criaacao.com',
    'https://criaacao.com/portfolio',
    'https://criaacao.com/quem-somos',
    'https://criaacao.com/solucoes',
    'https://criaacao.com/contato',
    'https://criaacao.com/eventos',
    'https://criaacao.com/trabalhe-conosco',
    'https://criaacao.com/solucoes/manual-do-verdadeiro-papai-noel',
    'https://criaacao.com/solucoes/shopping-centers',
    'https://criaacao.com/solucoes/gestao-publica',
    'https://criaacao.com/solucoes/escolas',
    'https://criaacao.com/solucoes/empresas-e-corporativo',
    'https://criaacao.com/solucoes/condominios-e-residencias',
    'https://criaacao.com/solucoes/buffets-e-espacos-de-eventos',
    'https://criaacao.com/solucoes/hospitais',
    'https://criaacao.com/solucoes/creches',
    'https://criaacao.com/solucoes/instituicoes-de-acolhimento'
]

today = datetime.datetime.now().strftime('%Y-%m-%d')

xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    priority = '1.0' if url == 'https://criaacao.com' else '0.8'
    xml_content += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>{priority}</priority>\n  </url>\n'
xml_content += '</urlset>\n'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(xml_content)
print('Sitemap generated.')
