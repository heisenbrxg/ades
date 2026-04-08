"""
Injects the style-6.css link (Century Gothic override) into all HTML files
that already include main.css, inserting it right after main.css.
"""

import os
import re

html_dir = os.path.dirname(os.path.abspath(__file__))
html_files = [f for f in os.listdir(html_dir) if f.endswith('.html')]

MAIN_CSS_PATTERN = re.compile(
    r'(<link[^>]+href=["\']assets/css/main\.css["\'][^>]*>)',
    re.IGNORECASE
)

STYLE6_LINK = '\n    <link rel="stylesheet" href="assets/css/style-6.css">'
STYLE6_CHECK = 'style-6.css'

updated = []
skipped = []

for filename in html_files:
    filepath = os.path.join(html_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if STYLE6_CHECK in content:
        skipped.append(filename)
        continue

    if MAIN_CSS_PATTERN.search(content):
        new_content = MAIN_CSS_PATTERN.sub(r'\1' + STYLE6_LINK, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated.append(filename)
    else:
        skipped.append(filename + ' (no main.css link found)')

print(f"\n✅ Updated {len(updated)} files:")
for f in sorted(updated):
    print(f"   - {f}")

print(f"\n⏭  Skipped {len(skipped)} files:")
for f in sorted(skipped):
    print(f"   - {f}")
