import os
import re

directory = r"e:\ades rework\ades\buyer-file"
files = [f for f in os.listdir(directory) if f.endswith(".html") and f != "index.html"]

def fix_content(content):
    # 1. Split content into Header/Body and Footer to avoid breaking footer which is STILL dark
    parts = re.split(r'(<footer)', content, flags=re.IGNORECASE)
    if len(parts) < 2:
        return content
    
    body = parts[0]
    remainder = "".join(parts[1:])
    
    # -- Fixes for Body Area --
    
    # Replace text-white class with text-dark or remove it (outside of footer)
    body = body.replace('text-white', 'text-dark')
    
    # Handle specific transparency that was meant for dark mode
    body = body.replace('rgba(255, 255, 255, 0.05)', 'rgba(0, 0, 0, 0.04)')
    body = body.replace('rgba(255, 255, 255, 0.08)', 'rgba(0, 0, 0, 0.06)')
    body = body.replace('rgba(255, 255, 255, 0.15)', 'rgba(0, 0, 0, 0.1)')
    
    # Fix specific styles in text_invert classes if any
    body = body.replace('linear-gradient(to right, #fff 50%, #fff 50%)', 'linear-gradient(to right, #000 50%, #000 50%)')
    
    # 2. Re-remove dark.css just in case
    body = re.sub(r'<link rel="stylesheet" href="assets/css/dark.css">', '', body)
    
    # 3. Ensure footer background remains dark (as per previous fix)
    remainder = re.sub(
        r'footer\.footer-area-four \.footer-wrapper \{[\s\S]*?background: rgba\(255, 255, 255, 0\.04\) !important;',
        r'footer.footer-area-four .footer-wrapper {\n            background: #111 !important;',
        remainder
    )
    
    return body + remainder

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = fix_content(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Fixed visibility on {len(files)} sub-pages.")
