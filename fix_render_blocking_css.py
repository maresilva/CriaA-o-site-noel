import os
import glob
from bs4 import BeautifulSoup

def fix_css():
    html_files = glob.glob('*.html') + glob.glob('solucoes/*.html')
    
    # CSS that should remain render-blocking to avoid massive FOUC
    critical_css = [
        'typography.css',
        'design-system.css',
        'wp-global-styles.css',
        'header-global.css',
        'be.css',
        'responsive.css'
    ]
    
    count = 0
    for file in html_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(file, 'r', encoding='latin-1') as f:
                content = f.read()
                
        soup = BeautifulSoup(content, 'html.parser')
        modified = False
        
        # Find all stylesheets
        links = soup.find_all('link', rel='stylesheet')
        
        for link in links:
            href = link.get('href', '')
            
            # Skip if it's already deferred or preloaded
            if link.get('media') == 'print' or link.get('onload') or not href:
                continue
                
            # Check if it's in the critical list
            is_critical = any(c in href for c in critical_css)
            
            if not is_critical:
                # Defer the CSS
                link['media'] = 'print'
                link['onload'] = "this.media='all'"
                
                # Add noscript fallback right after the link
                noscript = soup.new_tag('noscript')
                fallback_link = soup.new_tag('link', rel='stylesheet', href=href)
                if link.get('id'):
                    fallback_link['id'] = link.get('id') + '-fallback'
                noscript.append(fallback_link)
                link.insert_after(noscript)
                
                modified = True
        
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            count += 1
            print(f"Fixed render-blocking CSS in {file}")

    print(f"Done! Modified {count} files.")

if __name__ == '__main__':
    fix_css()
