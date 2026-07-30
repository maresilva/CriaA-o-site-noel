import os
import re
from bs4 import BeautifulSoup
from PIL import Image

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

# Map old source to new source and dimensions
processed_images = {}

def clean_filename(filename):
    name, ext = os.path.splitext(filename)
    # Remove timestamps like _1783720420891
    name = re.sub(r'_\d+$', '', name)
    # Replace underscores with hyphens
    name = name.replace('_', '-')
    # Keep it clean
    return f"{name}.webp"

for filepath in files:
    if not os.path.exists(filepath):
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
            
    soup = BeautifulSoup(content, 'html.parser')
    modified = False
    
    # Calculate directory depth to resolve relative paths
    base_dir = os.path.dirname(filepath)
    
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if not src or src.startswith('http') or src.startswith('data:'):
            continue
            
        # Resolve path
        if src.startswith('../'):
            local_src = src.replace('../', '')
        else:
            if base_dir:
                local_src = os.path.join(base_dir, src).replace('\\', '/')
            else:
                local_src = src
                
        # If it's an SVG, skip conversion, just add attributes
        is_svg = local_src.lower().endswith('.svg')
        
        if not is_svg and os.path.exists(local_src):
            if local_src not in processed_images:
                try:
                    with Image.open(local_src) as p_img:
                        width, height = p_img.size
                        
                        # Prepare new path
                        dirname = os.path.dirname(local_src)
                        basename = os.path.basename(local_src)
                        new_basename = clean_filename(basename)
                        new_local_src = os.path.join(dirname, new_basename).replace('\\', '/')
                        
                        # Convert to WebP
                        if not os.path.exists(new_local_src):
                            p_img.save(new_local_src, 'webp', quality=85)
                            
                        processed_images[local_src] = {
                            'new_local': new_local_src,
                            'width': width,
                            'height': height,
                            'new_basename': new_basename
                        }
                except Exception as e:
                    print(f"Error processing {local_src}: {e}")
                    
            if local_src in processed_images:
                info = processed_images[local_src]
                
                # Update src
                # Keep the relative prefix `../` if it existed
                if src.startswith('../'):
                    new_src = '../' + info['new_local']
                else:
                    if base_dir:
                        new_src = info['new_local'].replace(base_dir + '/', '')
                    else:
                        new_src = info['new_local']
                        
                img['src'] = new_src
                
                # Add width and height
                if not img.get('width'):
                    img['width'] = str(info['width'])
                if not img.get('height'):
                    img['height'] = str(info['height'])
                    
                # Fix ALT
                alt = img.get('alt')
                if alt is None or alt.strip() == '':
                    if 'cookies' in info['new_basename'].lower():
                        img['alt'] = ''
                    else:
                        clean_alt = info['new_basename'].replace('.webp', '').replace('-', ' ').title()
                        img['alt'] = clean_alt
                        
                modified = True
                
        # Add Lazy Loading / FetchPriority
        if 'logo-criaacao-entretenimento' in src.lower():
            img['fetchpriority'] = 'high'
            # Remove lazy if it was added
            if img.get('loading') == 'lazy':
                del img['loading']
            modified = True
        else:
            if not img.get('loading'):
                img['loading'] = 'lazy'
                modified = True
                
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Optimized images in {filepath}")

# Delete old files
deleted_count = 0
for old_path in processed_images.keys():
    if old_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
            os.remove(old_path)
            deleted_count += 1
        except:
            pass

print(f"Optimization complete. Converted {len(processed_images)} images and deleted {deleted_count} old files.")
