import os

folder = 'solucoes'
for filename in os.listdir(folder):
    if filename.endswith('.html'):
        filepath = os.path.join(folder, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content.replace('<a href="./">Home</a>', '<a href="../">Home</a>')
        new_content = new_content.replace('<a href="./solucoes">Soluções</a>', '<a href="../solucoes">Soluções</a>')
        
        # in case it was modified:
        new_content = new_content.replace('<a href="./">HOME</a>', '<a href="../">HOME</a>')
        new_content = new_content.replace('<a href="./solucoes">SOLUÇÕES</a>', '<a href="../solucoes">SOLUÇÕES</a>')

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed {filepath}')
