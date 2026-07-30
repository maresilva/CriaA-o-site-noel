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

def audit_images():
    report = {
        'total_images': 0,
        'missing_alt': [],
        'missing_dimensions': [],
        'missing_lazy_loading': [],
        'legacy_formats': set(),
        'bad_filenames': set()
    }
    
    for filepath in files:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        for img in soup.find_all('img'):
            report['total_images'] += 1
            src = img.get('src', '')
            
            # Check alt
            alt = img.get('alt')
            if alt is None or alt.strip() == '':
                report['missing_alt'].append({'file': filepath, 'src': src})
                
            # Check dimensions
            if not img.get('width') or not img.get('height'):
                report['missing_dimensions'].append({'file': filepath, 'src': src})
                
            # Check lazy loading (only if not a critical hero image, but for audit we just flag missing ones)
            if not img.get('loading'):
                report['missing_lazy_loading'].append({'file': filepath, 'src': src})
                
            # Check format
            lower_src = src.lower()
            if lower_src.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                report['legacy_formats'].add(src)
                
            # Check filename (spaces, special chars)
            filename = os.path.basename(src)
            if ' ' in filename or '%' in filename or '_' in filename:
                report['bad_filenames'].add(src)

    report['legacy_formats'] = list(report['legacy_formats'])
    report['bad_filenames'] = list(report['bad_filenames'])
    
    with open('image_audit_results.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

audit_images()
print("Image audit complete.")
