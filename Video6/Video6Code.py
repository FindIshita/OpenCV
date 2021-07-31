import cv2
import numpy as np
# Importing libraries
img = cv2.imread('bookpage.jpg')
# Importing image on which thresholding is to be applied.
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
# Inside the brackets, first the source is named (which has to be in grayscale), followed by the thresholding value,
# maximum value and the thresholding technique applied. The basic working is that all the pixel values above the
# threshold value are converted to maximum threshold value, while all those below the threshold value are converted
# to 0.
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# This step simply converts the taken image to grayscale for all the thresholding techniques which are about to come.
retval2, threshold_gray = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
# The same simple thresholding is applied again. But this time we apply it on a grayscaled image. The result
# difference can be seen in the output.
threshold_adaptive = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
# Adaptive thresholding is used when different areas have different amount of lighting which makes it difficult for
# simple thresholding to work effectively. Here, the values are calculated for smaller areas hence, different areas
# with different lighting get different threshold values. Firstly, with cv2.adaptiveThreshold we tell the system
# about the method we are going to use. Inside the brackets, we first define the source (has to be grayscaled),
# maximum value, the type of adaptive method which we will use (here we take the Gaussian weighted sum of the
# neighbour pixels, alternatively we can also take the mean as per the case), followed by the type of thresholding,
# the number of neighbour pixels which we want to include in the calculation and a constant which is subtracted from
# the weighted sum (or mean).
retval3,threshold_otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Inside the brackets, the source (always grayscaled), the threshold value ( above and below which the pixel values
# will be changed), the max value and the type of threhsolding is determined.
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold_gray',threshold_gray)
cv2.imshow('threshold_adaptive',threshold_adaptive)
cv2.imshow('threshold_otsu',threshold_otsu)
# Output the images
cv2.waitKey(0)
cv2.destroyAllWindows()