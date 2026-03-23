import os
import re

directory = r"e:\ades rework\ades\buyer-file"
files = [f for f in os.listdir(directory) if f.endswith(".html") and f != "index.html"]

def audit_nav(content, filename):
    results = []
    
    # Check for glass-nav
    if 'class="glass-nav"' not in content:
        results.append("MISSING glass-nav class")
    
    # Check for hover color fix
    if '.glass-nav .nav-links .dropdown a:hover' in content:
        if 'color: white !important' not in content and 'color:white !important' not in content:
            results.append("OLD hover color (#111)")
            
    # Check for dropdowns
    if 'href="service-mep.html"' not in content:
        results.append("MISSING Services dropdown items")
    if 'href="team.html"' not in content:
        results.append("MISSING Company dropdown")
    if 'href="project-1.html"' not in content and filename not in ['project-1.html', 'project-2.html']:
         if 'Projects <i' not in content:
             results.append("MISSING Projects dropdown")
             
    # Check for "About Us" vs "About"
    if '>About Us</a>' in content:
        results.append("HAS 'About Us' instead of 'About'")
        
    return results

print(f"{'Filename':<30} | {'Issues'}")
print("-" * 60)
for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = audit_nav(content, filename)
    if issues:
        print(f"{filename:<30} | {', '.join(issues)}")
    else:
        # print(f"{filename:<30} | OK")
        pass
