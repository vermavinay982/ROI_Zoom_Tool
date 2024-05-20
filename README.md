# ROI Zoom Tool
For research papers, we need to present zoomed segment of image, this tool can create it easily and its written in opencv - so can be changed as per usage. Its an initial version of tool

### Input
![Image](assets/cat.png)

### Output
![Image](zoomroi_output_cat_bbox_210_203_376_317.png)

Output has coordinates for future use: "zoomroi_output_cat_bbox_210_203_376_317.png"


## Common Errors

1. File Not Found, or Incorrect File Type Selected: OpenCV(4.9.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:1272: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvShowImage'
 
 
    
    Fix: 
    - pip uninstall opencv-python-headless
    - pip uninstall opencv-python
    - pip install opencv-python