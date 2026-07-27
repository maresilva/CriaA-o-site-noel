import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

style_ids = [
    'wp-emoji-styles-inline-css',
    'classic-theme-styles-inline-css',
    'global-styles-inline-css',
    'mfn-dynamic-inline-css',
    'mfn-custom-inline-css'
]

css = ''
for style_id in style_ids:
    pattern = re.compile(f'<style id=\"{style_id}\">(.*?)</style>', re.DOTALL | re.IGNORECASE)
    match = pattern.search(content)
    if match:
        css += f'/* --- {style_id} --- */\n' + match.group(1) + '\n\n'
        content = content[:match.start()] + content[match.end():]

kit_path = 'assets/css/80ad7b0867ffd0f4_post-52.css'
try:
    with open(kit_path, 'r', encoding='utf-8') as f:
        css += '/* --- elementor-kit-52 --- */\n' + f.read() + '\n\n'
except:
    pass

if 'wp-global-styles.css' not in content:
    head_end = content.find('</head>')
    if head_end != -1:
        link_tag = '\n  <link rel=\"stylesheet\" href=\"assets/css/wp-global-styles.css\">\n'
        content = content[:head_end] + link_tag + content[head_end:]

with open('assets/css/wp-global-styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
