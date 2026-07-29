import os

files = ['index.html', 'portfolio.html']
old_img = "assets/images/portfolio/imagem-do-papai-noel-shopping-parangaba-criacao-entretenimento.png"
new_img = "assets/images/portfolio/imagem-do-papai-noel-north-shopping-criaacao-entretenimento.png"

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(old_img, new_img)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated image in {file}")
