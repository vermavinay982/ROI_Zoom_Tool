# CURRENT PROCESS
# read the image
# ask the user to select the ROI
# zoom the ROI part equal to that of image
# stack it horizontally and write the image. 
# a gui to enable selection of image file
# writing the image, with bbox coordinates

# FUTURE ADDITIONS
# allow user to save the coordinates, so can generate more using past coordinates
# to resize the zoomed portion to fit max width or height
# to choose custom color for portions


import tkinter as tk
from tkinter import filedialog
import os 

import cv2
import numpy as np

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)

try:
    img = cv2.imread(file_path)
    if img is None:
        raise ValueError

    r = cv2.selectROI("Select the Area", img) 
    x1, y1 = int(r[0]), int(r[1])
    x2, y2 = int(r[0]+r[2]), int(r[1]+r[3])
    cropped_image = img[y1:y2,x1:x2] 
    
    start_point = (x1, y1) 
    end_point = (x2, y2)
    color = (0, 255, 0) 
    thickness = 2
    img = cv2.rectangle(img, start_point, end_point, color, thickness) 

    h, w, c = img.shape
    print(img.shape)
    cropped_image = cv2.resize(cropped_image, (w,h))

    # Display cropped image 
    # cv2.imshow("Cropped image", cropped_image); cv2.waitKey(0) 
    cv2.destroyWindow('Select the Area')

    new_img = np.hstack([img, cropped_image])
    
    cv2.imshow("New image", new_img) 
    cv2.waitKey(0) 

    new_path = f"zoomroi_output_{os.path.basename(file_path).split('.')[0]}_bbox_{x1}_{y1}_{x2}_{y2}.png"
    write_flag = cv2.imwrite(new_path, new_img)
    if write_flag:
        print(f"Image written at: {new_path} Successfully")
    else:
        print(f"Failed to write Image: old:{file_path} new:{new_path}")


except Exception as e:
    print(f"File Not Found, or Incorrect File Type Selected: {e}")
