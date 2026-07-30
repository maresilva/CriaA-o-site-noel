import os
import json
from bs4 import BeautifulSoup

def audit_mobile_seo():
    report = {
        'viewport_tags': {}
    }

    files = ['index.html', 'portfolio.html', 'quem-somos.html']

    for filepath in files:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        viewport = soup.find('meta', attrs={'name': 'viewport'})
        if viewport:
            report['viewport_tags'][filepath] = viewport.get('content')
        else:
            report['viewport_tags'][filepath] = 'Missing'

    with open('mobile_audit_results.json', 'w') as f:
        json.dump(report, f, indent=2)

audit_mobile_seo()
print("Mobile SEO audit complete.")
