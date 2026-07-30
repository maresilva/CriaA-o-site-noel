import os
import json
from bs4 import BeautifulSoup
import glob

def audit_schema():
    report = {}
    
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

    for filepath in files:
        if not os.path.exists(filepath):
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                
            schemas = soup.find_all('script', type='application/ld+json')
            
            parsed_schemas = []
            for s in schemas:
                try:
                    data = json.loads(s.string)
                    parsed_schemas.append(data)
                except Exception as e:
                    parsed_schemas.append({'error': 'Invalid JSON', 'raw': s.string})
                    
            if parsed_schemas:
                report[filepath] = parsed_schemas
            else:
                report[filepath] = []
                
        except Exception as e:
            report[filepath] = [{'error': str(e)}]
            
    with open('schema_audit_results.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

audit_schema()
print("Schema audit complete.")
