import numpy as np
import cv2
# Importing libraries
img = cv2.imread('corner_image.jpg')
# Importing the image whose corners have to be detected.
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Convert to grayscale.
gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# This finds the corners of the image by Shi-Tomasi method. The image has to be in grayscale for this. Inside the
# brackets, we specify the source, maximum corners to be found, quality level and the minimum distance in order.
corners = np.int0(corners)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, (0,255,255), -1)
    # We make circle around each corner of the specified radius and color, thickness etc.
cv2.imshow('Corner', img)
cv2.waitKey()
cv2.destroyAllWindows()