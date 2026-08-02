import os
import glob
import re
import json
from bs4 import BeautifulSoup

html_files = glob.glob('*.html') + glob.glob('solucoes/*.html')

BASE_URL = 'https://www.criaacao.com'
LOGO_URL = f'{BASE_URL}/assets/images/gallery/nossa-historia-criaacao-entretenimento.jpg'
COMPANY_NAME = 'CriaAção Entretenimento'
COMPANY_DESC = 'Empresa especializada em experiências natalinas para Shopping Centers e grandes empreendimentos.'

def build_schema(filepath, soup):
    title = soup.title.string if soup.title else COMPANY_NAME
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc['content'] if meta_desc else COMPANY_DESC
    
    filename = filepath.replace('\\', '/')
    if filename == 'index.html':
        url = f'{BASE_URL}/'
    else:
        url = f'{BASE_URL}/{filename.replace(".html", "")}'
        
    graph = []
    
    # ORGANIZATION
    org = {
        "@type": "Organization",
        "@id": f"{BASE_URL}/#organization",
        "name": COMPANY_NAME,
        "url": f"{BASE_URL}/",
        "logo": {
            "@type": "ImageObject",
            "@id": f"{BASE_URL}/#logo",
            "url": LOGO_URL,
            "width": 1200,
            "height": 800,
            "caption": COMPANY_NAME
        },
        "image": {"@id": f"{BASE_URL}/#logo"},
        "description": COMPANY_DESC,
        "slogan": "A maior empresa de Natal para Shopping Centers.",
        "telephone": "+5585988601400",
        "email": "marcos.criacao@gmail.com",
        "areaServed": ["BR"],
        "knowsAbout": [
            "Natal para Shopping Centers",
            "Cenografia Natalina para Shoppings",
            "Papai Noel Profissional para Empreendimentos",
            "Experiências Temáticas de Natal",
            "Projetos Natalinos de Alto Padrão"
        ]
    }
    graph.append(org)
    
    # LOCAL BUSINESS
    local_business = {
        "@type": "LocalBusiness",
        "@id": f"{BASE_URL}/#localbusiness",
        "name": COMPANY_NAME,
        "url": f"{BASE_URL}/",
        "telephone": "+5585988601400",
        "parentOrganization": {"@id": f"{BASE_URL}/#organization"},
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Fortaleza",
            "addressRegion": "CE",
            "addressCountry": "BR"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": -3.731862,
            "longitude": -38.52667
        },
        "image": {"@id": f"{BASE_URL}/#logo"},
        "priceRange": "$$$"
    }
    graph.append(local_business)
    
    # WEBSITE
    website = {
        "@type": "WebSite",
        "@id": f"{BASE_URL}/#website",
        "url": f"{BASE_URL}/",
        "name": COMPANY_NAME,
        "description": COMPANY_DESC,
        "publisher": {"@id": f"{BASE_URL}/#organization"}
    }
    graph.append(website)
    
    # WEBPAGE
    webpage = {
        "@type": "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": title,
        "description": description,
        "isPartOf": {"@id": f"{BASE_URL}/#website"},
        "about": {"@id": f"{BASE_URL}/#organization"},
        "primaryImageOfPage": {"@id": f"{BASE_URL}/#logo"}
    }
    graph.append(webpage)
    
    # BREADCRUMB
    breadcrumb = {
        "@type": "BreadcrumbList",
        "@id": f"{url}#breadcrumb",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": f"{BASE_URL}/"
            }
        ]
    }
    
    if filename != 'index.html':
        if '/' in filename:
            breadcrumb["itemListElement"].append({
                "@type": "ListItem",
                "position": 2,
                "name": "Soluções",
                "item": f"{BASE_URL}/solucoes"
            })
            page_name = filename.split('/')[-1].replace('.html', '').replace('-', ' ').title()
            breadcrumb["itemListElement"].append({
                "@type": "ListItem",
                "position": 3,
                "name": page_name,
                "item": url
            })
        else:
            page_name = filename.replace('.html', '').replace('-', ' ').title()
            breadcrumb["itemListElement"].append({
                "@type": "ListItem",
                "position": 2,
                "name": page_name,
                "item": url
            })
            
    webpage["breadcrumb"] = {"@id": f"{url}#breadcrumb"}
    graph.append(breadcrumb)
    
    # SERVICE (If it's a solucoes subpage)
    if 'solucoes/' in filename and filename != 'solucoes.html':
        service = {
            "@type": "Service",
            "@id": f"{url}#service",
            "name": title,
            "description": description,
            "provider": {"@id": f"{BASE_URL}/#organization"},
            "areaServed": {"@id": f"{BASE_URL}/#localbusiness"},
            "serviceType": "Projetos Natalinos e Experiências Temáticas",
            "audience": {
                "@type": "Audience",
                "audienceType": "Shopping Centers e grandes empreendimentos"
            }
        }
        graph.append(service)
        
    return {
        "@context": "https://schema.org",
        "@graph": graph
    }


def main():
    count = 0
    # regex to find application/ld+json blocks
    json_ld_pattern = re.compile(r'<script[^>]*type=[\"\'\s]*application/ld\+json[\"\'\s]*[^>]*>(.*?)</script>', re.IGNORECASE | re.DOTALL)
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        
        new_schema = build_schema(filepath, soup)
        new_json_str = json.dumps(new_schema, ensure_ascii=False, indent=2)
        new_script_tag = f'<script type="application/ld+json">\n{new_json_str}\n  </script>'
        
        # We assume there is only one ld+json script in the original file
        if json_ld_pattern.search(html):
            new_html = json_ld_pattern.sub(new_script_tag, html, count=1)
            # if there are multiple for some reason, remove the rest
            while json_ld_pattern.search(new_html, new_html.find('</script>', new_html.find(new_script_tag))):
                # find the index after our new script
                idx = new_html.find(new_script_tag) + len(new_script_tag)
                new_html = new_html[:idx] + json_ld_pattern.sub('', new_html[idx:])
        else:
            # If no json_ld found, append to head
            new_html = html.replace('</head>', f'  {new_script_tag}\n</head>')

        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            f.write(new_html)
        count += 1

    print(f'Processed {count} files.')

if __name__ == '__main__':
    main()
