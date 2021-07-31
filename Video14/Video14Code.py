import numpy as np
import cv2
import matplotlib.pyplot as plt
# Importing libraries.
img1 = cv2.imread('img_2.png',0)
# Reading the template.
img2 = cv2.imread('img_1.png',0)
# Reading the image.
orb = cv2.ORB_create()
# orb is the detector we are going to use. So here, we initialise it.
kp1, des1 = orb.detectAndCompute(img1,None)
# These are query key-points and query descriptors and inside the brackets we specify the source and type "None".
kp2, des2 = orb.detectAndCompute(img2,None)
# These are train key-points and train descriptors and again the source and type 'None' is specified.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# The method used is specified while crossCheck is True.
matches = bf.match(des1,des2)
# Using the query descriptor and train descriptor the bf is initialised for matching and matching occurs.
matches = sorted(matches, key = lambda x:x.distance)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:30],None, flags=2)
# Matches to the final image are drawn using the image, query and train key-points and train descriptor.
plt.imshow(img3)
# Final image is shown.
plt.show()