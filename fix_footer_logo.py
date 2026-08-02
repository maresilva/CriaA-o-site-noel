import glob

files = glob.glob('solucoes/*.html')
count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace('src="./assets/logos/logo-criaacao-entretenimento.webp"', 'src="../assets/logos/logo-criaacao-entretenimento.webp"')
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8', newline='') as file:
            file.write(new_content)
        count += 1
print(f'Fixed footer logo in {count} files.')
