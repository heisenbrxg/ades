import cv2
import numpy as np
import os

images = ['fsb_mechanical.png', 'fsb_electrical.png', 'fsb_phe_fps.png', 'fsb_elv_ibms.png']
base_path = r'e:\ades rework\ades rework\ades\buyer-file\assets\img'

for img_name in images:
    img_path = os.path.join(base_path, img_name)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Could not load {img_name}")
        continue
    
    # Calculate variance of pixel intensities across each row
    variances = np.var(img, axis=1)
    
    # Find rows with very low variance (solid color lines)
    solid_rows = np.where(variances < 10)[0]
    
    if len(solid_rows) > 0:
        print(f"{img_name}: potential horizontal solid lines at rows: {solid_rows[0]} to {solid_rows[-1]}, out of {img.shape[0]} total rows")
    else:
        print(f"{img_name}: No solid lines detected.")
