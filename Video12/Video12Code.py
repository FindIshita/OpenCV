import cv2
import numpy as np
# Importing libraries
img_rgb = cv2.imread('opencv_image.png')
# Importing the image
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# Converting the image to grayscale.
template = cv2.imread('template.png',0)
# Importing the template.
w, h = template.shape[::-1]
# 'w' and 'h' store the width and height of the template respectively.
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# In this function, we first specify that we want to perform template matching. The parameters are the image which
# has to be matched, the template which has to be used as the reference and the method of template matching.
threshold = 0.7
# Setting up the threshold. When the template and image are compared and the result is greater than the threshold
# then the object is said to be detected, otherwise not.
loc = np.where( res >= threshold)
# The co-ordinates of the area which is matched is stored.
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1)
    # This simply draws a rectangle around the stored co-ordinates with the desired color and thickness.
cv2.imshow('Matched',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()