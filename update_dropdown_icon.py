import glob
import re
import os

old_css = r"""<style>
\.ca-has-dropdown \{ position: relative; \}
\.ca-dropdown-menu \{ display: none; position: absolute; top: 100%; left: 0; background: rgba\(26,5,10,0\.95\); min-width: 260px; padding: 10px 0; margin: 0; list-style: none; border-top: 2px solid #D4AF37; box-shadow: 0 5px 20px rgba\(0,0,0,0\.5\); z-index: 999; backdrop-filter: blur\(10px\); \}
\.ca-has-dropdown:hover \.ca-dropdown-menu \{ display: block; \}
\.ca-dropdown-menu li \{ padding: 0 !important; margin: 0 !important; \}
\.ca-dropdown-menu li a \{ display: block; padding: 12px 20px !important; color: #fff !important; font-size: 14px !important; text-transform: none !important; text-decoration: none; transition: 0\.3s; line-height: 1\.4; font-weight: normal; \}
\.ca-dropdown-menu li a:hover \{ color: #D4AF37 !important; background: rgba\(212,175,55,0\.1\); \}
@media \(max-width: 980px\) \{
  \.ca-dropdown-menu \{ position: static; background: transparent; box-shadow: none; border-top: none; padding-left: 15px; \}
  \.ca-has-dropdown:hover \.ca-dropdown-menu \{ display: block; \}
\}
</style>"""

new_css = """<style>
.ca-has-dropdown { position: relative; }
.ca-has-dropdown > a { display: inline-flex !important; align-items: center; }
.ca-has-dropdown > a::after { content: ""; display: inline-block; margin-left: 8px; width: 6px; height: 6px; border-right: 1.5px solid currentColor; border-bottom: 1.5px solid currentColor; transform: rotate(45deg); transition: transform 0.3s ease; margin-top: -2px; }
.ca-has-dropdown:hover > a::after { transform: rotate(225deg); margin-top: 4px; }
.ca-dropdown-menu { display: none; position: absolute; top: 100%; left: 0; background: rgba(26,5,10,0.95); min-width: 260px; padding: 10px 0; margin: 0; list-style: none; border-top: 2px solid #D4AF37; box-shadow: 0 5px 20px rgba(0,0,0,0.5); z-index: 999; backdrop-filter: blur(10px); }
.ca-has-dropdown:hover .ca-dropdown-menu { display: block; }
.ca-dropdown-menu li { padding: 0 !important; margin: 0 !important; }
.ca-dropdown-menu li a { display: block; padding: 12px 20px !important; color: #fff !important; font-size: 14px !important; text-transform: none !important; text-decoration: none; transition: 0.3s; line-height: 1.4; font-weight: normal; }
.ca-dropdown-menu li a:hover { color: #D4AF37 !important; background: rgba(212,175,55,0.1); }
.ca-dropdown-menu li a::after { display: none !important; } /* Prevent caret on submenu links */
@media (max-width: 980px) {
  .ca-dropdown-menu { position: static; background: transparent; box-shadow: none; border-top: none; padding-left: 15px; }
  .ca-has-dropdown:hover .ca-dropdown-menu { display: block; }
}
</style>"""

html_files = glob.glob("*.html")

# also checking inside solucoes/manual-do-verdadeiro-papai-noel.html
if os.path.exists('solucoes/manual-do-verdadeiro-papai-noel.html'):
    html_files.append('solucoes/manual-do-verdadeiro-papai-noel.html')

for file in html_files:
    if file == 'design_system1.html' or file.startswith('scratch'): continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will just replace the exact block if it exists
    # To handle potential whitespace differences, we can also use a simpler replacement strategy
    # If we just replace the start of the style block:
    
    if ".ca-has-dropdown { position: relative; }" in content and ".ca-has-dropdown > a::after" not in content:
        # Find the block and replace it
        start_marker = "<style>\n.ca-has-dropdown { position: relative; }"
        end_marker = "}\n</style>"
        
        idx_start = content.find(start_marker)
        if idx_start != -1:
            idx_end = content.find(end_marker, idx_start) + len(end_marker)
            if idx_end != -1:
                content = content[:idx_start] + new_css + content[idx_end:]
                
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Added caret icon to {file}")
            
print("Done.")
