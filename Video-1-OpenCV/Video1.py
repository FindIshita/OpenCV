import cv2
import numpy as np
import matplotlib.pyplot as plt
# These are libraries we need to import.
img = cv2.imread('OpenCVimg.jpg', cv2.IMREAD_GRAYSCALE)
# Two parameters are specified path and flag. path = Represents the path of the image. Flag = It can be of three
# types color, grayscale and unchanged.Color tells to load a color image. Grayscale tells the image to load in gray
# mode. Unchanged specifies to load an image as it is.
plt.imshow(img, cmap='gray', interpolation='bicubic')
# Cmap customises the colormap to gray.
plt.plot((50, 100), [100, 240], 'c', linewidth=7)
# The above parameter specifies the start, end , color and thickness of the plot.
plt.show()
cv2.imshow('image', img)
# image is the name of window and the "img" defined above is shown.
cv2.waitKey(0)
# Closes the window after the time (in ms) is over after pressing any key.
cv2.destroyAllWindows()
# Removes the window from screen.
