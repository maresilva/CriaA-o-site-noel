import re
import sys

def update_padding():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Dictionary of class patterns and their replacement paddings
    # Targeting the main block of each section class
    
    replacements = [
        # .ca-clients-section
        (r'(\.ca-clients-section\s*\{[^}]*padding:\s*)([0-9]+px(\s+[0-9]+px)*)(;)', r'\g<1>60px 20px\g<4>'),
        
        # .ca-portfolio-section
        (r'(\.ca-portfolio-section\s*\{[^}]*padding:\s*)([0-9]+px(\s+[0-9]+px)*)(\s*!important;)', r'\g<1>60px 20px\g<4>'),
        
        # .ca-segmentos-section
        (r'(\.ca-segmentos-section\s*\{[^}]*padding:\s*)([0-9]+px(\s+[0-9]+px)*)(;)', r'\g<1>60px 20px\g<4>'),
        
        # .ca-timeline-section
        (r'(\.ca-timeline-section\s*\{[^}]*padding:\s*)([0-9]+px(\s+[0-9]+px)*)(;)', r'\g<1>60px 20px\g<4>'),
        
        # .faq-section
        (r'(\.faq-section\s*\{[^}]*padding:\s*)([0-9]+px(\s+[0-9]+px)*)(;)', r'\g<1>60px 0\g<4>'),
        
        # .final-cta-section
        (r'(\.final-cta-section\s*\{[^}]*padding:\s*)([0-9]+px(\s+[0-9]+px)*)(\s*!important;)', r'\g<1>60px 20px\g<4>'),
        
        # .inst-contact-section
        (r'(\.inst-contact-section\s*\{[^}]*padding:\s*)([0-9]+px(\s+[0-9]+px)*)(;)', r'\g<1>60px 20px\g<4>'),
        
        # .ca-section (Generic class)
        (r'(\.ca-section\s*\{[^}]*padding:\s*)([0-9]+px(\s+[0-9]+px)*)(\s*!important;)', r'\g<1>60px 20px\g<4>'),
        
        # .ca-diferenciais-section might have an inline style padding or CSS block not found before
        # Let's target any inline padding="120px 20px" or similar on a section
        # We will do this separately
    ]

    new_content = content
    for pattern, repl in replacements:
        new_content = re.sub(pattern, repl, new_content, flags=re.IGNORECASE)

    # Specific check for ca-diferenciais-section
    # The screenshot showed section#diferenciais.ca-diferenciais-section with padding 120px 20px
    # Let's find any inline padding on section elements
    new_content = re.sub(r'(<section[^>]*style="[^"]*padding:\s*)120px(\s+20px;[^"]*">)', r'\g<1>60px\g<2>', new_content, flags=re.IGNORECASE)
    
    # Also in case inline styles were without semicolons
    new_content = re.sub(r'(<section[^>]*style="[^"]*padding:\s*)120px(\s+20px"?\s*[^>]*>)', r'\g<1>60px\g<2>', new_content, flags=re.IGNORECASE)

    if new_content != content:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated padding successfully.")
    else:
        print("No changes made. Patterns might not have matched.")

if __name__ == "__main__":
    update_padding()
