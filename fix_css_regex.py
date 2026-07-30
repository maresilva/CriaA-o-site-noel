import os
import glob
import re

def fix_css():
    html_files = glob.glob('*.html') + glob.glob('solucoes/*.html')
    
    # CSS that should remain render-blocking
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
                
        original_content = content
        
        # 1. Fix malformed noscript tags
        content = re.sub(
            r'<noscript><link href="([^"]+)" id="([^"]+)" media="all"(?:</noscript>)+ rel="stylesheet"/>',
            r'<link href="\1" id="\2" media="print" onload="this.media=\'all\'" rel="stylesheet"/>',
            content
        )
        
        # 2. Find normal stylesheets
        # We need a function to conditionally replace
        def replace_link(match):
            full_match = match.group(0)
            m2 = re.search(r'href="([^"]+)"', full_match)
            href = m2.group(1) if m2 else ''
            
            # Skip if already deferred or preloaded
            if 'media="print"' in full_match or 'onload=' in full_match:
                return full_match
                
            # Skip critical css
            if any(c in href for c in critical_css):
                return full_match
                
            # Defer it
            # Replace media="all" with media="print" onload="this.media='all'"
            if 'media="all"' in full_match:
                return full_match.replace('media="all"', 'media="print" onload="this.media=\'all\'"')
            else:
                # Just insert it before rel="stylesheet"
                return full_match.replace('rel="stylesheet"', 'media="print" onload="this.media=\'all\'" rel="stylesheet"')

        # Match <link href="..." id="..." media="all" rel="stylesheet"/>
        # Or <link href="..." rel="stylesheet"/>
        # Using a regex that matches link tags for stylesheets
        content = re.sub(r'<link[^>]+rel="stylesheet"[^>]*>', replace_link, content)
        content = re.sub(r'<link[^>]+href="[^"]+\.css"[^>]*>', replace_link, content)
        
        if content != original_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f"Fixed {file}")

    print(f"Done! Modified {count} files.")

if __name__ == '__main__':
    fix_css()
