from PIL import Image
import os

imgs = ['fsb_mechanical.png', 'fsb_electrical.png', 'fsb_phe_fps.png', 'fsb_elv_ibms.png']
for i in imgs:
    path = os.path.join(r"e:\ades rework\ades rework\ades\buyer-file\assets\img", i)
    img = Image.open(path)
    print(f"{i}: {img.size}")
