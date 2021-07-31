import cv2
import numpy as np
# Importing libraries
img_rgb = cv2.imread('opencv-template-matching-python-tutorial.jpg')
# Importing the image
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# Converting to grayscale.
template = cv2.imread('opencv-template-for-matching.jpg',0)
# Importing the template.
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
cv2.imshow('Detected',img_rgb)