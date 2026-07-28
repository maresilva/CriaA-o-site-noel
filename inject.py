import re

index = open('index.html', 'r', encoding='utf-8').read()
footer = re.search(r'(<!-- START INSTITUTIONAL CONTACT SECTION -->.*?<!-- End Footer Template -->\s*</div>)', index, re.DOTALL)
if footer:
    footer_html = footer.group(1)
    eventos = open('eventos.html', 'r', encoding='utf-8').read()
    if 'START INSTITUTIONAL CONTACT SECTION' not in eventos:
        eventos = re.sub(r'(<div id="body_overlay"></div>)', footer_html + r'\n\n\1', eventos)
        open('eventos.html', 'w', encoding='utf-8').write(eventos)
        print('Footer successfully injected into eventos.html')
    else:
        print('Footer already in eventos.html')
else:
    print('Footer not found in index.html')
