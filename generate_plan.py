import json

with open('seo_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

plan = "# SEO Technical & Accessibility Implementation Plan\n\n"
plan += "## User Review Required\n"
plan += "> [!IMPORTANT]\n> Please review the structural changes below. No layout or visual styles will be affected. These changes focus purely on semantic HTML and accessibility.\n\n"

plan += "## Proposed Changes\n\n"

for file, data in report.items():
    plan += f"### {file}\n\n"
    
    # 1. H1 Count
    h1s = [h['text'] for h in data['headings'] if h['tag'] == 'h1']
    if len(h1s) != 1:
        plan += f"- **H1 Tag Issue**: File has {len(h1s)} H1 tags. (SEO best practice is exactly one).\n"
        plan += f"  - Current H1s: {', '.join(h1s)}\n"
        plan += f"  - *Fix*: Keep the main title as H1 and convert others to H2.\n"
        
    # 2. Heading Hierarchy
    levels = [int(h['tag'][1]) for h in data['headings']]
    skipped = False
    for i in range(1, len(levels)):
        if levels[i] - levels[i-1] > 1:
            skipped = True
            break
    if skipped:
        plan += f"- **Heading Hierarchy**: Skipped heading levels detected (e.g., jumping from H2 to H4).\n"
        plan += f"  - *Fix*: Adjust heading levels to ensure logical sequential order without skipping.\n"
        
    # 3. Accessibility Issues
    a11y = data.get('a11y_issues', [])
    if a11y:
        plan += f"- **Accessibility & Labels**:\n"
        # group them
        inputs = [i for i in a11y if 'Input/Textarea' in i]
        links = [i for i in a11y if 'link' in i]
        
        if inputs:
            plan += f"  - {len(inputs)} form fields are missing `<label>` tags or `aria-label` attributes.\n"
            plan += f"  - *Fix*: Add `aria-label` or properly linked `<label for=\"...\">` to each input (e.g., {inputs[0].split(' ')[1]}).\n"
        if links:
            plan += f"  - Icon-only or empty links found missing `aria-label`.\n"
            plan += f"  - *Fix*: Add descriptive `aria-label` (e.g., 'WhatsApp' or 'Menu') to these `<a>` tags.\n"
            
    # 4. Landmarks
    landmarks = data.get('landmarks', {})
    if landmarks.get('main', 0) != 1:
        plan += f"- **Landmarks**: Missing or multiple `<main>` tags (Found {landmarks.get('main', 0)}).\n"
        plan += f"  - *Fix*: Wrap the primary content in exactly one `<main>` tag.\n"
        
    if landmarks.get('header', 0) > 1:
         plan += f"- **Landmarks**: Multiple `<header>` tags found (Found {landmarks.get('header', 0)}).\n"
         
    plan += "\n"

plan += "## Verification Plan\n"
plan += "### Automated Tests\n"
plan += "- Re-run the `seo_audit.py` script to verify that:\n"
plan += "  1. All pages have exactly one H1.\n"
plan += "  2. All inputs have labels/aria-labels.\n"
plan += "  3. No empty links exist without aria-labels.\n"
plan += "  4. Each page has exactly one `<main>` landmark.\n"

with open('C:\\Users\\gilma\\.gemini\\antigravity-ide\\brain\\9005844e-b627-4981-9208-ce543088285d\\implementation_plan.md', 'w', encoding='utf-8') as f:
    f.write(plan)
    
print("Plan generated")
