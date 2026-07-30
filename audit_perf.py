import os
import glob
import json
from bs4 import BeautifulSoup

def audit_performance():
    report = {
        'css_files': [],
        'js_files': [],
        'fonts': [],
        'render_blocking_js': [],
        'vercel_cache': False,
        'preconnects': []
    }

    # Find CSS and JS
    for css in glob.glob('assets/css/*.css'):
        report['css_files'].append(css.replace('\\', '/'))
        
    for js in glob.glob('assets/js/*.js'):
        report['js_files'].append(js.replace('\\', '/'))
        
    # Check HTML
    files = glob.glob('*.html') + glob.glob('*/*.html')
    files = [f for f in files if 'assets' not in f and 'scratch' not in f and 'design' not in f and 'header' not in f and 'missing' not in f and 'new_segment' not in f and 'google' not in f and '404' not in f]

    for filepath in files:
        if not os.path.exists(filepath):
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                
            # Scripts in head
            if soup.head:
                for script in soup.head.find_all('script', src=True):
                    # Exclude GTM which is explicitly handled
                    if 'googletagmanager' not in script['src']:
                        if not script.get('defer') and not script.get('async'):
                            report['render_blocking_js'].append({'file': filepath, 'src': script['src']})
                            
            # Preconnects
            for link in soup.find_all('link', rel='preconnect'):
                if link.get('href') not in report['preconnects']:
                    report['preconnects'].append(link.get('href'))
                    
            # Fonts
            for link in soup.find_all('link', rel='stylesheet'):
                href = link.get('href', '')
                if 'fonts.googleapis' in href:
                    if href not in report['fonts']:
                        report['fonts'].append(href)
                        
        except Exception as e:
            pass

    # Check vercel.json
    if os.path.exists('vercel.json'):
        with open('vercel.json', 'r') as f:
            content = f.read()
            if 'Cache-Control' in content:
                report['vercel_cache'] = True

    with open('perf_audit_results.json', 'w') as f:
        json.dump(report, f, indent=2)

audit_performance()
print("Perf audit complete.")
