import os
import glob

html_files = glob.glob("*.html")
if not html_files:
    # Also check subdirectories if any, but they are all in root
    pass

old_css = """                  .ca-dropdown-menu {
                    position: static;
                    background: transparent;
                    box-shadow: none;
                    border-top: none;
                    padding-left: 15px;
                    margin-top: 0;
                  }

                  .ca-dropdown-menu::before {
                    display: none;
                  }

                  .ca-has-dropdown:hover .ca-dropdown-menu,
                  .ca-has-dropdown.is-active .ca-dropdown-menu {
                    display: block;
                  }"""

new_css = """                  .ca-dropdown-menu {
                    position: static !important;
                    background: transparent !important;
                    box-shadow: none !important;
                    border-top: none !important;
                    padding-left: 15px !important;
                    margin-top: 0 !important;
                    display: none;
                  }

                  .ca-dropdown-menu::before {
                    display: none !important;
                  }

                  .ca-has-dropdown:hover .ca-dropdown-menu,
                  .ca-has-dropdown.is-active .ca-dropdown-menu,
                  #Side_slide .ca-has-dropdown.is-active .ca-dropdown-menu {
                    display: block !important;
                    visibility: visible !important;
                    opacity: 1 !important;
                    height: auto !important;
                  }"""

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_css in content:
        content = content.replace(old_css, new_css)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Could not find exact CSS block in {file}")
