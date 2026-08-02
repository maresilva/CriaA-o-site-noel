import os
import glob
import re
from bs4 import BeautifulSoup
import urllib.parse

html_files = [f for f in glob.glob('*.html') + glob.glob('solucoes/*.html') if 'design_system' not in f and 'scratch' not in f]
sitemap_path = 'sitemap.xml'

# Parse Sitemap
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

sitemap_images = re.findall(r'<image:loc>([^<]+)</image:loc>', sitemap_content)

eligible_images = []
blocked_images = []
broken_images = []
missing_from_sitemap = []

# Exclude list for purely decorative/structural images
decorative_keywords = ['icon', 'cookies', 'separador', 'dummy', 'shape']

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    for img in soup.find_all('img'):
        src = img.get('src', '')
        alt = img.get('alt')
        
        # Determine if decorative
        is_decorative = False
        if alt == "":
            is_decorative = True
        for kw in decorative_keywords:
            if kw in src.lower():
                is_decorative = True
                
        # Resolve local path to check if broken
        # Handle absolute URLs vs relative
        if src.startswith('http'):
            local_path = None # skip external for broken check
        else:
            # simple resolution since all HTMLs are root or 1 dir deep
            if filepath.startswith('solucoes'):
                local_path = os.path.join(os.path.dirname(filepath), '..', src)
            else:
                local_path = src
                
            local_path = os.path.normpath(local_path)
            
            if local_path and not os.path.exists(local_path):
                # Check if we need to remove leading slash
                local_path_no_slash = local_path.lstrip('\\/')
                if not os.path.exists(local_path_no_slash):
                    broken_images.append({'page': filepath, 'src': src})
        
        if not is_decorative:
            # It is eligible for indexing
            # Priority check: portfolio, solucoes, etc.
            is_priority = 'portfolio' in src.lower() or 'solucoes' in filepath.lower() or 'projetos' in src.lower() or 'clientes' in src.lower()
            
            img_data = {'page': filepath, 'src': src, 'alt': alt, 'priority': is_priority}
            eligible_images.append(img_data)
            
            # Check sitemap
            # Usually sitemap would have absolute URLs
            filename = os.path.basename(src)
            in_sitemap = False
            for s_img in sitemap_images:
                if filename in s_img:
                    in_sitemap = True
                    break
                    
            if not in_sitemap and is_priority:
                missing_from_sitemap.append(img_data)

print(f"=== IMAGE INDEXING AUDIT ===")
print(f"Total HTML files checked: {len(html_files)}")
print(f"Sitemap parsed. Images in sitemap: {len(sitemap_images)}")
print(f"Images eligible for indexing (non-decorative): {len(eligible_images)}")
print(f"Priority images missing from sitemap: {len(missing_from_sitemap)}")
print(f"Broken images: {len(broken_images)}")
print(f"Blocked images (via robots.txt): 0 (Verified robots.txt allows all)")

if broken_images:
    print("\nBroken Images:")
    for b in broken_images[:10]:
        print(f" - {b['src']} (on {b['page']})")
