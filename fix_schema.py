import os
import json
from bs4 import BeautifulSoup

files_data = {
    'index.html': { 'name': 'CriaAção Entretenimento', 'title': 'Soluções de Natal para Shoppings e Empresas | CriaAção', 'url': 'https://criaacao.com/' },
    'portfolio.html': { 'name': 'Portfólio', 'title': 'Portfólio | Projetos e Eventos de Natal | CriaAção', 'url': 'https://criaacao.com/portfolio' },
    'quem-somos.html': { 'name': 'Quem Somos', 'title': 'Quem Somos | Nossa História com o Natal | CriaAção', 'url': 'https://criaacao.com/quem-somos' },
    'solucoes.html': { 'name': 'Soluções', 'title': 'Soluções de Natal para Shoppings | CriaAção', 'url': 'https://criaacao.com/solucoes' },
    'contato.html': { 'name': 'Contato', 'title': 'Contato | Solicite Orçamento de Eventos | CriaAção', 'url': 'https://criaacao.com/contato' },
    'eventos.html': { 'name': 'Eventos', 'title': 'Eventos de Natal e Datas Comemorativas | CriaAção', 'url': 'https://criaacao.com/eventos' },
    'solucoes/manual-do-verdadeiro-papai-noel.html': { 'name': 'Manual do Verdadeiro Papai Noel', 'title': 'Manual do Verdadeiro Papai Noel | Treinamento | CriaAção', 'url': 'https://criaacao.com/solucoes/manual-do-verdadeiro-papai-noel' },
    'trabalhe-conosco.html': { 'name': 'Trabalhe Conosco', 'title': 'Trabalhe Conosco | Seja Papai Noel | CriaAção', 'url': 'https://criaacao.com/trabalhe-conosco' },
}

org_schema = {
    "@type": "Organization",
    "@id": "https://criaacao.com/#organization",
    "name": "CriaAção Entretenimento",
    "url": "https://criaacao.com/",
    "logo": "https://criaacao.com/assets/images/gallery/nossa-historia-criaacao-entretenimento.webp",
    "areaServed": "BR",
    "knowsAbout": "Eventos Natalinos para Shopping Centers"
}

local_schema = {
    "@type": "LocalBusiness",
    "@id": "https://criaacao.com/#localbusiness",
    "name": "CriaAção Entretenimento",
    "url": "https://criaacao.com/",
    "telephone": "+5585988601400",
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Fortaleza",
        "addressRegion": "CE",
        "addressCountry": "BR"
    },
    "areaServed": "BR",
    "priceRange": "$",
    "parentOrganization": { "@id": "https://criaacao.com/#organization" }
}

for filepath, meta in files_data.items():
    if not os.path.exists(filepath):
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

    # Remove all old schemas
    for script in soup.find_all('script', type='application/ld+json'):
        script.decompose()

    # Build new graph
    graph = [org_schema, local_schema]
    
    # WebSite vs WebPage
    if filepath == 'index.html':
        graph.append({
            "@type": "WebSite",
            "@id": "https://criaacao.com/#website",
            "url": "https://criaacao.com/",
            "name": meta['title'],
            "publisher": { "@id": "https://criaacao.com/#organization" }
        })
    else:
        graph.append({
            "@type": "WebPage",
            "@id": meta['url'] + "/#webpage",
            "url": meta['url'],
            "name": meta['title'],
            "isPartOf": { "@id": "https://criaacao.com/#website" }
        })

    # Breadcrumb
    breadcrumb_items = [{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://criaacao.com/"
    }]
    
    if filepath != 'index.html':
        if filepath == 'solucoes/manual-do-verdadeiro-papai-noel.html':
            breadcrumb_items.append({
                "@type": "ListItem",
                "position": 2,
                "name": "Soluções",
                "item": "https://criaacao.com/solucoes"
            })
            breadcrumb_items.append({
                "@type": "ListItem",
                "position": 3,
                "name": meta['name'],
                "item": meta['url']
            })
        else:
            breadcrumb_items.append({
                "@type": "ListItem",
                "position": 2,
                "name": meta['name'],
                "item": meta['url']
            })

    graph.append({
        "@type": "BreadcrumbList",
        "itemListElement": breadcrumb_items
    })

    schema_payload = {
        "@context": "https://schema.org",
        "@graph": graph
    }
    
    # Inject new schema
    new_script = soup.new_tag('script', type='application/ld+json')
    new_script.string = json.dumps(schema_payload, indent=2, ensure_ascii=False)
    if soup.head:
        soup.head.append(new_script)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"Fixed schema in {filepath}")

print("Schema fix complete.")
