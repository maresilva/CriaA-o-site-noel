import os
import glob
import re
from PIL import Image
import json

# Configurations
html_files = glob.glob('*.html') + glob.glob('solucoes/*.html')
image_files = glob.glob('assets/images/**/*.*', recursive=True)

print("--- 1. IMAGE MAPPING & CONVERSION ---")
converted_count = 0
heavy_images_report = []

for img_path in image_files:
    size_kb = os.path.getsize(img_path) / 1024
    if size_kb > 300 and img_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
            with Image.open(img_path) as img:
                width, height = img.size
                format_orig = img.format
                
                is_logo = 'logo' in img_path.lower()
                is_photo = not is_logo
                
                recommended_format = 'WebP' if is_photo else 'PNG'
                
                # We will convert it if it's a photo
                new_size = size_kb
                if is_photo:
                    webp_path = os.path.splitext(img_path)[0] + '.webp'
                    if not os.path.exists(webp_path):
                        img.save(webp_path, 'WEBP', quality=85)
                    
                    if os.path.exists(webp_path):
                        new_size = os.path.getsize(webp_path) / 1024
                        converted_count += 1
                        
                heavy_images_report.append({
                    'file': img_path,
                    'format': format_orig,
                    'size_kb': round(size_kb, 2),
                    'width': width,
                    'height': height,
                    'is_photo': is_photo,
                    'recommended_format': recommended_format,
                    'estimated_new_size_kb': round(new_size, 2)
                })
        except Exception as e:
            print(f"Error processing {img_path}: {e}")

# Save report
with open('heavy_images_report.json', 'w', encoding='utf-8') as f:
    json.dump(heavy_images_report, f, indent=2)

print(f"Total heavy images mapped: {len(heavy_images_report)}")
print(f"Total images converted to WebP: {converted_count}")

print("\n--- 2. HTML OPTIMIZATION (Safe Regex) ---")

def process_img_tag(img_tag_orig, filepath, html_content):
    img_tag = img_tag_orig
    
    src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag, re.IGNORECASE)
    if not src_match:
        return img_tag_orig
        
    src = src_match.group(1)
    local_src = src.lstrip('./').lstrip('../')
    
    # 2. Add width and height if missing
    if 'width=' not in img_tag and 'height=' not in img_tag:
        if os.path.exists(local_src):
            try:
                with Image.open(local_src) as i:
                    img_tag = img_tag.replace('<img ', f'<img width="{i.width}" height="{i.height}" ')
            except:
                pass
                
    # 3. LCP and Lazy loading
    is_lcp = False
    idx = html_content.find(img_tag_orig)
    context_before = html_content[max(0, idx-500):idx].lower()
    
    if 'hero' in context_before or 'banner' in context_before or 'sc-hero' in img_tag_orig:
        is_lcp = True
    elif idx < 2000 and 'logo' not in src.lower(): 
        is_lcp = True
        
    is_header_footer = 'logo' in src.lower() or 'header' in context_before or 'footer' in context_before or 'nav' in context_before
    
    if is_lcp:
        img_tag = re.sub(r'\sloading=["\']lazy["\']', '', img_tag, flags=re.IGNORECASE)
        if 'fetchpriority' not in img_tag:
            img_tag = img_tag.replace('<img ', '<img fetchpriority="high" ')
    else:
        if not is_header_footer and 'loading=' not in img_tag:
             img_tag = img_tag.replace('<img ', '<img loading="lazy" ')
             
    # 4. Wrap in picture if WebP exists
    webp_local = os.path.splitext(local_src)[0] + '.webp'
    if os.path.exists(webp_local) and not src.lower().endswith('.webp'):
        webp_src = os.path.splitext(src)[0] + '.webp'
        picture_tag = f'<picture>\n  <source srcset="{webp_src}" type="image/webp">\n  {img_tag}\n</picture>'
        if '<picture>' not in context_before[-20:]: 
            return picture_tag
            
    return img_tag

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    new_html = html
    
    # 5. Fonts Optimization
    if 'fonts.googleapis.com' in new_html:
        if '<link rel="preconnect" href="https://fonts.googleapis.com">' not in new_html:
            preconnects = '<link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  '
            new_html = new_html.replace('</title>', f'</title>\n  {preconnects}')
            
        new_html = re.sub(r'(href=["\']https://fonts\.googleapis\.com/css2\?[^"\']+)(["\'])', 
                          lambda m: m.group(1) + ('&display=swap' if 'display=swap' not in m.group(1) else '') + m.group(2), 
                          new_html)

    img_tags = re.findall(r'<img[^>]+>', new_html, re.IGNORECASE)
    
    for img_tag_orig in set(img_tags): 
        replacement = process_img_tag(img_tag_orig, filepath, new_html)
        if replacement != img_tag_orig:
            new_html = new_html.replace(img_tag_orig, replacement)

    if new_html != html:
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            f.write(new_html)
        print(f"Optimized: {filepath}")

print("\nPerformance Phase 1 Execution Completed.")
