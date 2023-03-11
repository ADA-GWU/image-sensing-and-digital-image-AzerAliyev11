# Assignment 1 - Image Sensing and Digital Image

This assignment is about converting an image into various types (grayscale, black-white, etc.) and also determining the close colors on the object
and background of the image.  
It was required to work with 4 images:  
  * Image taken in a daylight during the day (high light)
  * Image taken in a daylight in the evening (low light)
  * Image taken under a bright fluorescent light
  * Image taken under a dim fluorescent light  
  
These images are saved in the **Images** folder.  
### GrayImages Folder 
**GrayImages** folder contains the results of the images that are converted into grayscale.  
### DiscImages Folder 
**DiscImages** folder contains the results of the images that are discretized.  
### BlackWhite Folder 
**BlackWhite** folder contains the results of the images that are converted into black-and-white.  
### ChangedHSL Folder 
**ChangedHSL** folder contains the results of the images that have their HSL values changed.  
### CloseColors Folder 
**CloseColors** folder contains the results of the images showing all of the close colors (indicated with green pixels) on the background and
on the object itself. All of the results are named properly and saved separately. Naming convention is [LightSource][Close]_[Type]
(FluoDimClose_Back for close colors on the background of the image taken under dim fluorescent light)  


Threshold value is 10 for finding close colors since this number yielded better results comparatively.

## main.py
All the code is contained inside the **main.py** file. The code is well commented. Converting an image into grayscale and finding close colors on
an image are written inside functions **GrayConverter** and **find_close_colors**  


None of the results are being shown to the user with imshow since all of the results are being saved in their corresponding folders. Apart from that,
these folders are generated on the root location of the **main.py** through the code itself.  


It takes significant amount of time to compute the close colors since the images are of high resolution. Therefore,
images are being resized to a smaller size and then they are processed through the find_close_colors function.
