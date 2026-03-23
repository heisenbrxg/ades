import os
import re

directory = r"e:\ades rework\ades\buyer-file"
files = [f for f in os.listdir(directory) if f.endswith(".html") and f != "index.html"]

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove dark.css link
    content = re.sub(r'<link rel="stylesheet" href="assets/css/dark.css">', '', content)
    
    # 2. Update glass footer background to solid dark
    content = re.sub(
        r'footer\.footer-area-four \.footer-wrapper \{[\s\S]*?background: rgba\(255, 255, 255, 0\.04\) !important;',
        r'footer.footer-area-four .footer-wrapper {\n            background: #111 !important;',
        content
    )
    
    # 3. Remove dark-bg class from body
    content = re.sub(r'<body class="dark-bg">', '<body>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(files)} sub-pages.")
