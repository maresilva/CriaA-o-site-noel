import os
import json
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

geo_tags = [
    '<meta name="geo.region" content="BR-CE" />',
    '<meta name="geo.placename" content="Fortaleza" />',
    '<meta name="geo.position" content="-3.731862;-38.526670" />',
    '<meta name="ICBM" content="-3.731862, -38.526670" />'
]

for filepath in files:
    if not os.path.exists(filepath):
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

    modified = False

    # 1. Add Geo Meta Tags
    if soup.head:
        head_str = str(soup.head)
        if 'geo.region' not in head_str:
            for tag in reversed(geo_tags):
                tag_soup = BeautifulSoup(tag, 'html.parser').meta
                soup.head.insert(0, tag_soup)
            modified = True

    # 2. Update Schema
    for script in soup.find_all('script', type='application/ld+json'):
        try:
            data = json.loads(script.string)
            if '@graph' in data:
                for item in data['@graph']:
                    if item.get('@type') == 'LocalBusiness':
                        if 'geo' not in item:
                            item['geo'] = {
                                "@type": "GeoCoordinates",
                                "latitude": -3.731862,
                                "longitude": -38.526670
                            }
                            item['openingHoursSpecification'] = {
                                "@type": "OpeningHoursSpecification",
                                "dayOfWeek": [
                                    "Monday",
                                    "Tuesday",
                                    "Wednesday",
                                    "Thursday",
                                    "Friday"
                                ],
                                "opens": "08:00",
                                "closes": "18:00"
                            }
                            script.string = json.dumps(data, indent=2, ensure_ascii=False)
                            modified = True
        except Exception as e:
            pass

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Fixed local SEO in {filepath}")

print("Local SEO fix complete.")
