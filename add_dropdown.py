import glob
import re

css_code = """<style>
.ca-has-dropdown { position: relative; }
.ca-dropdown-menu { display: none; position: absolute; top: 100%; left: 0; background: rgba(26,5,10,0.95); min-width: 260px; padding: 10px 0; margin: 0; list-style: none; border-top: 2px solid #D4AF37; box-shadow: 0 5px 20px rgba(0,0,0,0.5); z-index: 999; backdrop-filter: blur(10px); }
.ca-has-dropdown:hover .ca-dropdown-menu { display: block; }
.ca-dropdown-menu li { padding: 0 !important; margin: 0 !important; }
.ca-dropdown-menu li a { display: block; padding: 12px 20px !important; color: #fff !important; font-size: 14px !important; text-transform: none !important; text-decoration: none; transition: 0.3s; line-height: 1.4; font-weight: normal; }
.ca-dropdown-menu li a:hover { color: #D4AF37 !important; background: rgba(212,175,55,0.1); }
@media (max-width: 980px) {
  .ca-dropdown-menu { position: static; background: transparent; box-shadow: none; border-top: none; padding-left: 15px; }
  .ca-has-dropdown:hover .ca-dropdown-menu { display: block; }
}
</style>
"""

new_menu_item = """<li class="ca-has-dropdown"><a href="solucoes.html">SOLU&Ccedil;&Otilde;ES</a>
  <ul class="ca-dropdown-menu">
    <li><a href="solucoes/manual-do-verdadeiro-papai-noel">Manual do Verdadeiro Papai Noel</a></li>
  </ul>
</li>"""

html_files = glob.glob("*.html")

for file in html_files:
    if file == 'design_system1.html' or file.startswith('scratch'): continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'class="ca-has-dropdown"' in content:
        print(f"Skipping {file}, dropdown already exists.")
        continue
        
    # Replace the Soluções menu item
    # Since there can be spaces, we use a regex
    content = re.sub(r'<li>\s*<a href="solucoes\.html">SOLU&Ccedil;&Otilde;ES</a>\s*</li>', new_menu_item, content, flags=re.IGNORECASE)
    
    # Inject the CSS right before the </nav> tag of the menu
    content = re.sub(r'(</nav>)', css_code + r'\1', content, count=1, flags=re.IGNORECASE)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {file}")

print("Done updating dropdown.")
