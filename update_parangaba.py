import os

file = 'portfolio.html'
old_img = "assets/images/gallery/desktop-papai-noel-na-poltrona-criaacao-entretenimento.jpg"
new_img = "assets/images/portfolio/imagem-trono-do-papai-noel-shopping-parangaba-criaacao-entretenimento.png"

if os.path.exists(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(old_img, new_img)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated image in {file}")
