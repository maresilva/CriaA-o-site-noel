import os
import re

# 1. Update button styles across multiple files
files_to_update = ['index.html', 'solucoes.html', 'quem-somos.html', 'portfolio.html']

old_style = 'style="display: flex; justify-content: center; align-items: center; gap: 12px; width: 100%; background: linear-gradient(90deg, #D4AF37 0%, #F3E5AB 50%, #D4AF37 100%); color: #1a050a; padding: 18px 24px; border-radius: 12px; font-weight: 700; text-decoration: none; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(212,175,55,0.3); background-size: 200% auto; text-transform: uppercase; letter-spacing: 1px;"'
new_style = 'style="display: flex; justify-content: center; align-items: center; gap: 12px; width: 100%; background: linear-gradient(90deg, #D4AF37 0%, #F3E5AB 50%, #D4AF37 100%); color: #1a050a; padding: 18px 24px; border-radius: 12px; font-weight: 700; text-decoration: none; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(212,175,55,0.3); background-size: 200% auto; text-transform: uppercase; letter-spacing: 1px; box-sizing: border-box; max-width: 100%; white-space: normal; text-align: center;"'

for f in files_to_update:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        if old_style in content:
            content = content.replace(old_style, new_style)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated {f} with generic button fix.")

# 2. Update index.html specific styles (the inline style of CTA and the style block)
with open('index.html', 'r', encoding='utf-8') as file:
    index_content = file.read()

# Update inline CTA button in index.html
old_cta_inline = 'style="display: inline-flex; align-items: center; gap: 12px; background: linear-gradient(90deg, #D4AF37 0%, #F3E5AB 50%, #D4AF37 100%); color: #1a050a; padding: 16px 32px; border-radius: 100px; font-weight: 600; text-decoration: none; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(212,175,55,0.3); background-size: 200% auto;"'
new_cta_inline = 'style="display: inline-flex; align-items: center; justify-content: center; gap: 12px; background: linear-gradient(90deg, #D4AF37 0%, #F3E5AB 50%, #D4AF37 100%); color: #1a050a; padding: 16px 32px; border-radius: 100px; font-weight: 600; text-decoration: none; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(212,175,55,0.3); background-size: 200% auto; max-width: 100%; box-sizing: border-box; white-space: normal; text-align: center;"'
if old_cta_inline in index_content:
    index_content = index_content.replace(old_cta_inline, new_cta_inline)

# Update another CTA button in index.html
old_cta2_inline = 'style="display: inline-flex; align-items: center; justify-content: center; gap: 12px; background: linear-gradient(90deg, #D4AF37 0%, #F3E5AB 50%, #D4AF37 100%); color: #1a050a; padding: 16px 32px; border-radius: 100px; font-weight: 600; text-decoration: none; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(212,175,55,0.3); background-size: 200% auto;"'
if old_cta2_inline in index_content:
    index_content = index_content.replace(old_cta2_inline, new_cta_inline)

# Replace .ca-btn-glass block
old_glass_css = """      .ca-btn-glass {
        display: inline-flex;
        align-items: center;
        gap: 12px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #ffffff;
        padding: 16px 32px;
        border-radius: 100px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
      }"""
new_glass_css = """      .ca-btn-glass {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #ffffff;
        padding: 16px 32px;
        border-radius: 100px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        box-sizing: border-box;
        max-width: 100%;
        white-space: normal;
        text-align: center;
      }"""
if old_glass_css in index_content:
    index_content = index_content.replace(old_glass_css, new_glass_css)

old_contact_css = """      .final-cta-contact {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        color: rgba(255, 255, 255, 0.6);
        font-size: 1rem;
        transition: color 0.3s ease;
      }"""
new_contact_css = """      .final-cta-contact {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        color: rgba(255, 255, 255, 0.6);
        font-size: 1rem;
        transition: color 0.3s ease;
        box-sizing: border-box;
        max-width: 100%;
        white-space: normal;
        text-align: center;
        padding: 0 10px;
      }"""
if old_contact_css in index_content:
    index_content = index_content.replace(old_contact_css, new_contact_css)

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(index_content)
print("Updated index.html specific CTA styling.")
    
# 3. Add footer to eventos.html
with open('eventos.html', 'r', encoding='utf-8') as file:
    eventos_content = file.read()

# Extract footer from index.html
match = re.search(r'(<!-- START INSTITUTIONAL CONTACT SECTION -->.*?<!-- End Footer Template -->\s*</div>)', index_content, re.DOTALL)
if match:
    footer = match.group(1)
    if 'START INSTITUTIONAL CONTACT SECTION' not in eventos_content:
        pattern = r'(</script>\s*)(<style>\s*@media \(min-width: 981px\))'
        eventos_content = re.sub(pattern, r'\g<1>' + footer + r'\n          \g<2>', eventos_content)
        with open('eventos.html', 'w', encoding='utf-8') as file:
            file.write(eventos_content)
        print("Injected footer to eventos.html")
    else:
        print("Footer already in eventos.html")
else:
    print("Could not find footer in index.html to inject")
