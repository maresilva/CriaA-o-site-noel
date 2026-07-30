import os
import json
import re
from bs4 import BeautifulSoup

def audit_local_seo():
    report = {
        'geo_meta_tags': False,
        'has_google_maps': False,
        'phones_with_tel': [],
        'phones_without_tel': [],
        'addresses_found': [],
        'localbusiness_schema_complete': False
    }

    files = ['index.html', 'contato.html']

    for filepath in files:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        # Check Geo meta tags
        if soup.find('meta', attrs={'name': 'geo.region'}) or soup.find('meta', attrs={'name': 'geo.position'}):
            report['geo_meta_tags'] = True

        # Check Maps
        if soup.find('iframe', src=re.compile(r'google\.com/maps')):
            report['has_google_maps'] = True

        # Check Phones
        for a in soup.find_all('a', href=True):
            href = a['href']
            text = a.get_text(strip=True)
            if 'wa.me' in href or 'api.whatsapp' in href or 'tel:' in href:
                if 'tel:' in href:
                    report['phones_with_tel'].append(href)
                # Just tracking what exists

        # Check text for addresses (looking for Fortaleza, CE)
        text_content = soup.get_text()
        if 'Fortaleza' in text_content and 'CE' in text_content:
            # We'll just note it exists
            report['addresses_found'].append(filepath)

        # Check Schema
        schemas = soup.find_all('script', type='application/ld+json')
        for s in schemas:
            if 'LocalBusiness' in s.text:
                if 'geo' in s.text and 'openingHoursSpecification' in s.text:
                    report['localbusiness_schema_complete'] = True

    with open('local_seo_results.json', 'w') as f:
        json.dump(report, f, indent=2)

audit_local_seo()
print("Local SEO audit complete.")
