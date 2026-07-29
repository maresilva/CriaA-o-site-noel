import os

files = ['index.html', 'solucoes/manual-do-verdadeiro-papai-noel.html']
old_str = "mockup-manual-papai-noel.png"
new_str = "mockup-livro-manual-do-verdadeiro-papai-noel-criaacao-entretenimento.png"

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(old_str, new_str)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated image in {file}")
