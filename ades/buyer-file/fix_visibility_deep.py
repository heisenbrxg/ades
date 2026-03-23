import os
import re

directory = r"e:\ades rework\ades\buyer-file"
files = [f for f in os.listdir(directory) if f.endswith(".html") and f != "index.html"]

def fix_content(content):
    # Split into body and footer (footer should stay dark)
    parts = re.split(r'(<footer)', content, flags=re.IGNORECASE)
    if len(parts) < 2:
        return content
    
    body = parts[0]
    footer = "".join(parts[1:])
    
    # 1. Fix CSS in <style> tags
    # Replace white-based translucency with dark-based translucency for light mode
    body = re.sub(r'background:\s*rgba\(255,\s*255,\s*255,\s*0\.0[3-8]\)', 'background: rgba(0, 0, 0, 0.04)', body)
    body = re.sub(r'border: 1px solid rgba\(255, 255, 255, 0\.[0-2]\)', 'border: 1px solid rgba(0, 0, 0, 0.1)', body)
    body = body.replace('color: rgba(255, 255, 255, 0.7)', 'color: rgba(0, 0, 0, 0.7)')
    body = body.replace('color: white !important', 'color: #111 !important') # Specifically for FAQ etc.
    
    # 2. Fix Client Logo Filters (make them visible on white)
    body = body.replace('filter: grayscale(1) brightness(1.5)', 'filter: grayscale(1) brightness(0.5)')
    body = body.replace('opacity: 0.7', 'opacity: 0.8') # for logos
    
    # 3. Fix text classes in HTML
    body = body.replace('text-white', 'text-dark')
    body = body.replace('text-primary', 'text-primary') # Primary is usually okay (lime/yellow)
    
    # 4. Handle specific linear gradients that might be white-on-white
    body = body.replace('linear-gradient(to right, #fff 50%, #fff 50%)', 'linear-gradient(to right, #111 50%, #111 50%)')
    
    # 5. Ensure the body doesn't have "dark-bg" class
    body = body.replace('<body class="dark-bg">', '<body>')
    
    return body + footer

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = fix_content(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Deep fixed visibility on {len(files)} sub-pages.")
