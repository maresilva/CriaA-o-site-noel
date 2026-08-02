import os
import re

folder = 'solucoes'
for filename in os.listdir(folder):
    if filename.endswith('.html'):
        filepath = os.path.join(folder, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace href="./something" with href="../something"
        # Exception: do not replace href=".//" which might be some weird external link prefix
        # We will use regex to find href="./" not followed by "/"
        new_content = re.sub(r'href="\./(?!/)', 'href="../', content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed {filepath}')
