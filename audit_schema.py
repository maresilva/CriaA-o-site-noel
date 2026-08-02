import glob
import re

html_files = glob.glob('*.html') + glob.glob('solucoes/*.html')
json_ld_pattern = re.compile(r'<script[^>]*type=[\"\'\s]*application/ld\+json[\"\'\s]*[^>]*>(.*?)</script>', re.IGNORECASE | re.DOTALL)
microdata_pattern = re.compile(r'itemscope|itemtype|itemprop', re.IGNORECASE)
rdfa_pattern = re.compile(r'vocab|typeof|property=', re.IGNORECASE)

results = []

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_json_ld = bool(json_ld_pattern.search(content))
    has_microdata = bool(microdata_pattern.search(content))
    has_rdfa = bool(rdfa_pattern.search(content))
    
    if has_json_ld or has_microdata or has_rdfa:
        found = []
        if has_json_ld: found.append('JSON-LD')
        if has_microdata: found.append('Microdata')
        if has_rdfa: found.append('RDFa')
        
        j = ', '.join(found)
        results.append(f'{filepath}: {j}')
        
        # print first json-ld snippet
        match = json_ld_pattern.search(content)
        if match:
             print(f'\n--- JSON-LD in {filepath} ---')
             print(match.group(1).strip()[:200] + '...')

print('\nSummary of files with schema:')
if results:
    for r in results: print(r)
else:
    print('No structured data found in any HTML file.')
