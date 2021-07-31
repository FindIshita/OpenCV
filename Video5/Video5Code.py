import numpy as np
import cv2
# Import python libraries
img1 = cv2.imread('photo.jpg')
# Importing the fore-ground image.
img2 = cv2.imread('background.jpg')
# Importing the back-ground image.
rows,cols, channels = img1.shape
# This gives a tuple of rows, columns and channels (in case of color image). Shape of the image is found ith the help
# of this command.
roi = img2[100:rows, 100:cols]
# Region of background image is determined wherein we want the foreground image to be placed.
img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# The fore-ground image is converted to greyscale for simple thresholding in the next step.
ret, mask= cv2.threshold(img1gray, 1, 255, cv2.THRESH_BINARY_INV)
# Simple thresholding is done to obtain the mask of the image. Inside the brackets, first the source is named (which
# has to be in grayscale), followed by the thresholding value, maximum value and the thresholding technique applied.
# The basic working is that all the pixel values above the threshold value are converted to maximum threshold value,
# while all those below the threshold value are converted to 0. Hence, in this way we get a mask of the image. In
# thresh_binary_inv, the opposite of the above happens, which means all the values above the threshold value will be
# converted to 0 , while all those below it will be converted to 255.
mask_inv = cv2.bitwise_not(mask)
# Bitwise not operator reverses the present binary. In general case, it could be understood that 0 becomes 1 and 1
# become 0. So here the max value will be converted to 0 and vice versa.
img1_fg= cv2.bitwise_and(roi, roi, mask=mask)
# In bitwise and, only the pixels common between the two images are added up and the rest are removed from the
# output. Here, it is done to make the area of the fore-ground image as black.
img2_bg = cv2.bitwise_and(img1,img1, mask=mask_inv)
# This is done to just take the area of the fore-image and rest everything is black. Basically, the opposite of the
# above.
dst = cv2.add(img1_fg, img2_bg)
# The two images created above are added.
img2[100:rows, 100:cols] = dst
# The main image is modified.
cv2.imshow('dst', dst)
cv2.imshow('res', img2)
cv2.imshow('mask', mask_inv)
cv2.imshow('bg', img1_fg)
cv2.imshow('fg', img2_bg)
# Printing all the above stuff.
cv2.waitKey(0)
cv2.destroyAllWindows()