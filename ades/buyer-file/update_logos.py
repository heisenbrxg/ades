import glob
import os

files = glob.glob('*.html') + ['apply_nav.py']
count = 0
for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            data = file.read()
        
        new_data = data.replace('assets/img/logo/white-logo.svg', 'assets/img/A D E S.png')
        new_data = new_data.replace('assets/img/logo/black-logo.svg', 'assets/img/A D E S.png')
        
        if new_data != data:
            with open(f, 'w', encoding='utf-8', errors='ignore') as file:
                file.write(new_data)
            count += 1
            print(f"Updated {f}")

print(f"Total files updated: {count}")
