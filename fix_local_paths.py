import os
import re
import glob

# 1. Create directory
os.makedirs('solucoes', exist_ok=True)

# 2. Read the file
with open('manual-do-verdadeiro-papai-noel.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 3. Replace paths to make them relative to /solucoes/
# href="assets/ -> href="../assets/
content = re.sub(r'href="assets/', 'href="../assets/', content)
# src="assets/ -> src="../assets/
content = re.sub(r'src="assets/', 'src="../assets/', content)
# url('assets/ -> url('../assets/
content = re.sub(r"url\('assets/", "url('../assets/", content)
content = re.sub(r'url\("assets/', 'url("../assets/', content)

# href="index.html" -> href="../index.html"
html_files = glob.glob("*.html")
for hf in html_files:
    if hf == 'manual-do-verdadeiro-papai-noel.html': continue
    content = re.sub(rf'href="{hf}"', rf'href="../{hf}"', content)

# Write to new location
with open('solucoes/manual-do-verdadeiro-papai-noel.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created solucoes/manual-do-verdadeiro-papai-noel.html")

# 4. Update dropdown links in all HTML files in root
for file in html_files:
    if file.startswith('scratch') or file == 'manual-do-verdadeiro-papai-noel.html': continue
    with open(file, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Check if we need to replace the link
    if 'href="solucoes/manual-do-verdadeiro-papai-noel"' in file_content:
        file_content = file_content.replace('href="solucoes/manual-do-verdadeiro-papai-noel"', 'href="solucoes/manual-do-verdadeiro-papai-noel.html"')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(file_content)
        print(f"Updated dropdown link in {file}")
    
    if 'href="solucoes/manual-do-verdadeiro-papai-noel.html"' in file_content and file != 'manual-do-verdadeiro-papai-noel.html':
        # Just to handle if it was already replaced
        pass

# Now delete the original one in root so it's clean
os.remove('manual-do-verdadeiro-papai-noel.html')
print("Cleaned up root file.")
