import re
import os

pages = [
    'quem-somos.html', 'solucoes.html', 'portfolio.html', 
    'eventos.html', 'contato.html', 'trabalhe-conosco.html'
]

# We are going to replace padding values in style blocks and inline styles
# But we must skip the `#hero` element.
# The user wants 80px top and bottom for Desktop.

for page in pages:
    if not os.path.exists(page):
        continue
        
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # 1. Fix .inst-contact-section multi-line padding
    new_content = re.sub(r'(\.inst-contact-section\s*\{[^}]*padding:\s*)(160px|120px|100px)(\s+[0-9]+px)?(\s+[0-9]+px)?(\s+[0-9]+px)?', r'\g<1>80px\g<3>', new_content, flags=re.IGNORECASE)
    
    # 2. Fix inline styles on <section> with large padding
    # Example: style="padding: 100px 0;"
    new_content = re.sub(r'(<section[^>]*style="[^"]*padding:\s*)(100px|120px|140px|160px)(\s+[0-9a-zA-Z%]+;?[^"]*">)', r'\g<1>80px\g<3>', new_content, flags=re.IGNORECASE)
    
    # 3. General catch for any padding > 80px inside a class definition (excluding #hero)
    # This requires looking for 'padding: 120px 0 80px;' etc.
    # It's safer to target specific known classes or just replace 'padding: 120px 0 80px;' directly
    new_content = re.sub(r'(padding:\s*)(100px|120px|140px|160px)(\s+0\s+80px;)', r'\g<1>80px\g<3>', new_content, flags=re.IGNORECASE)

    # 4. If there's a padding-top or padding-bottom in CSS classes, let's fix them if they are >= 100px and NOT in #hero
    # Since regex can't easily parse CSS blocks, we use negative lookbehind/ahead or just simple replace.
    # We will replace all `padding: 120px 20px;` to `padding: 80px 20px;` if it doesn't say #hero.
    
    # Replace common patterns
    for val in ['100px', '120px', '140px', '160px']:
        # standard padding: 120px 20px; or padding: 120px 0;
        new_content = re.sub(r'(?<!#hero\.ca-hero-fixed \{)(?<!#hero \{)(?<!padding-top: )(?<!padding-bottom: )padding:\s*' + val + r'(\s+(?:20px|0))', r'padding: 80px\g<1>', new_content, flags=re.IGNORECASE)

    # Let's fix .inst-contact-section explicitly if it still has 160px
    new_content = re.sub(r'(\.inst-contact-section\s*\{[^\}]*)padding:\s*160px\s+20px\s+0px\s+20px;', r'\g<1>padding: 80px 20px;', new_content, flags=re.IGNORECASE)

    if new_content != content:
        with open(page, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated padding in {page}")
    else:
        print(f"No changes in {page}")
