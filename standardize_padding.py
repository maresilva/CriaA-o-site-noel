import re
import os

files = ['index.html', 'solucoes.html', 'quem-somos.html', 'portfolio.html', 'eventos.html', 'contato.html']

# The classes we want to standardize padding for
classes_to_update = [
    r'\.ca-section',
    r'\.sol-section',
    r'\.sol-section-alt',
    r'\.sol-segments-section',
    r'\.final-cta-section',
    r'\.ca-contato-section',
    r'\.ca-portfolio-section',
    r'\.qs-section',
    r'\.ev-section',
    r'\.ca-about-section'
]

def standardize(content):
    # Standardize CSS blocks
    for cls in classes_to_update:
        # Regex to find the CSS block for the specific class
        # It matches .class { ... padding: ... }
        # And replaces padding: [anything]; with padding: 80px 20px !important;
        # We need to make sure we don't accidentally match something else, so we do it in a loop
        
        # Find block
        pattern = re.compile(r'(' + cls + r'\s*{[^}]*?)(padding\s*:\s*[^;\}]+;)([^}]*})', re.DOTALL)
        content = pattern.sub(r'\1padding: 80px 20px !important;\3', content)

    # Also standardize inline paddings on <section> tags that use inline styles (very rare but possible)
    # E.g. <section style="padding: 100px 0; ...">
    # Wait, doing this via regex for inline styles can be risky, let's just stick to CSS classes first.
    return content

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            old_content = file.read()
        
        new_content = standardize(old_content)
        
        if new_content != old_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Updated {f}')

print("Done padding standardization.")
