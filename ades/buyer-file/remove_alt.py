import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        src = file.read()
    
    changed = False
    
    if 'alt="Mechanical - Cardiovascular / Respiratory System"' in src:
        src = src.replace('alt="Mechanical - Cardiovascular / Respiratory System"', 'alt="Cardiovascular / Respiratory System"')
        changed = True
        
    if 'alt="Electrical - Nervous System"' in src:
        src = src.replace('alt="Electrical - Nervous System"', 'alt="Nervous System"')
        changed = True
        
    if 'alt="PHE / FPS - Circulatory System"' in src:
        src = src.replace('alt="PHE / FPS - Circulatory System"', 'alt="Circulatory System"')
        changed = True
        
    if 'alt="ELV / IBMS - Endocrine / Cerebro Spinal Nervous System"' in src:
        src = src.replace('alt="ELV / IBMS - Endocrine / Cerebro Spinal Nervous System"', 'alt="Endocrine / Cerebro Spinal Nervous System"')
        changed = True
        
    if changed:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(src)
        print(f'Updated alt text in {f}')
