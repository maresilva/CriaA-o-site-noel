import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

classes = [
    'ca-clients-section', 'ca-countdown-section', 'ca-diferenciais-section', 
    'ca-portfolio-section', 'ca-segmentos-section', 'ca-timeline-section', 
    'faq-section', 'final-cta-section', 'inst-contact-section', 
    'institucional-section', 'ca-section'
]

print("CSS Definitions in index.html:")
for cls in classes:
    # Find CSS block for this class
    pattern = r'(\.' + cls + r'\s*\{[^}]+\})'
    matches = re.findall(pattern, content)
    for match in matches:
        print(match)
        print("-" * 40)
