import os
import re

directory = r"e:\ades rework\ades\buyer-file"
files = [f for f in os.listdir(directory) if f.endswith(".html")]

def audit_footer(content, filename):
    results = []
    
    # Count footer tags
    footer_count = len(re.findall(r'<footer', content, re.IGNORECASE))
    if footer_count > 1:
        results.append(f"Multiple footers ({footer_count})")
    elif footer_count == 0:
        results.append("NO footer found")
        
    # Check for glassmorphism classes
    if 'footer-area-four' not in content:
        results.append("MISSING footer-area-four class")
    if 'footer-wrapper' not in content:
        results.append("MISSING footer-wrapper class")
        
    # Check for alignment issues (check for text-start vs text-center in footer)
    if '<div class="row gy-4 text-start">' not in content and footer_count > 0:
        results.append("Old footer alignment (missing text-start row)")
        
    # Check for modern link structure
    if 'About ADES' not in content and footer_count > 0:
        results.append("Old footer content (missing 'About ADES')")
        
    return results

print(f"{'Filename':<30} | {'Issues'}")
print("-" * 80)
for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = audit_footer(content, filename)
    if issues or filename == "index.html":
        print(f"{filename:<30} | {', '.join(issues)}")
