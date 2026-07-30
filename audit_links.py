import os
import json
from bs4 import BeautifulSoup
import urllib.parse

def audit_links():
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
    
    report = {
        'broken_links': [],
        'external_links': [],
        'internal_links': [],
        'anchor_texts': [],
        'clean_url_violations': []
    }
    
    valid_paths = [f.replace('.html', '') for f in files]
    valid_paths = [p if p != 'index' else '' for p in valid_paths]
    # Also valid paths with .html
    valid_paths_html = files
    
    # Track incoming links for orphan check
    incoming_links = {f: 0 for f in files}

    for filepath in files:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        # Base folder depth for relative resolution
        depth = filepath.count('/')
        
        for a in soup.find_all('a', href=True):
            href = a['href']
            anchor_text = a.get_text(strip=True)
            
            # Anchor text audit
            if not anchor_text and not a.find('img') and not a.find('svg') and not a.get('aria-label'):
                report['anchor_texts'].append({'file': filepath, 'href': href, 'issue': 'Empty Anchor'})
            elif anchor_text.lower() in ['clique aqui', 'veja mais', 'saiba mais']:
                report['anchor_texts'].append({'file': filepath, 'href': href, 'issue': 'Generic Anchor', 'text': anchor_text})
                
            # Internal vs External
            if href.startswith('http') and 'criaacao.com' not in href and 'cria-a-o-site-noel' not in href:
                report['external_links'].append(href)
                continue
                
            if href.startswith('mailto:') or href.startswith('tel:'):
                continue
                
            if href.startswith('#'):
                continue
                
            # Clean URL normalization (remove query/hash)
            clean_href = href.split('#')[0].split('?')[0]
            if not clean_href:
                continue
                
            # If internal absolute domain, strip it
            if 'criaacao.com' in clean_href or 'cria-a-o-site-noel' in clean_href:
                parsed = urllib.parse.urlparse(clean_href)
                clean_href = parsed.path.lstrip('/')
                
            # Resolve relative paths
            if clean_href.startswith('../'):
                clean_href = clean_href.replace('../', '')
                
            # Strip leading slashes
            clean_href = clean_href.lstrip('/')
            
            report['internal_links'].append({'source': filepath, 'target': clean_href})
            
            # Check for Clean URL violations (links that still have .html)
            if clean_href.endswith('.html') and clean_href != 'index.html':
                report['clean_url_violations'].append({'file': filepath, 'href': href})
            
            # Check if broken (not mapping to any file)
            # clean_href could be 'contato', 'contato.html', etc.
            is_valid = False
            for vf in files:
                if clean_href == vf or clean_href == vf.replace('.html', '') or (clean_href == '' and vf == 'index.html'):
                    is_valid = True
                    incoming_links[vf] += 1
                    break
            
            if not is_valid:
                report['broken_links'].append({'source': filepath, 'target': href})

    report['orphans'] = [f for f, count in incoming_links.items() if count == 0 and f != 'index.html']
    
    with open('link_audit_results.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

audit_links()
print("Link audit complete.")
