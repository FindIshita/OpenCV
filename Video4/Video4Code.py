import cv2
import numpy as np
# Importing files.
img = cv2.imread('OpenCVimg.jpg', cv2.IMREAD_COLOR)
# Used to read the image with the use of path and flag. Here image is imported in original colors.
px = img[55, 55]
# Stores the color values of the region specified in the image.
print(px)
# Prints out the color values.
img[55, 55] = [100, 20, 100]
# We are changing the color values of the given pixel.
px = img[55, 55]
# Now the new values of color of the pixel is stored. So, the previous value gets over-written.
print(px)
# New value will be printed.
img[37:111, 107:194] = [100, 20, 100]
# This changes the color value of the entire Region Of Image which is defined within the square brackets.
Copy_image = img[300:400, 500:550]
# Image is copied from the the location specified within square brackets.
img[20:120, 20:70] = Copy_image
# Copied image is pasted at the location specified within the square brackets.
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Shows the image and closes the window on command.
