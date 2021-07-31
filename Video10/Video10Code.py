import cv2
import numpy as np
# Importing the libraries.
cap = cv2.VideoCapture(0)
# Using the first camera for the implementation.
while (1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # same steps as explained before hence did not repeat.
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    # Laplacian edge detectors work on the basis that if there is steep curve between two pixels meaning to say if
    # the neighbour pixels are very different from each other then the border is considered to be an edge. If one
    # side the curev is rising and on the other side it's falling, then in the middle there has to be an intersection
    # point (in the case of curve, a 0 point). That is considered to be an edge when working with laplacian edge
    # detectors. Inside the brackets, we specify where we want to add the filter and the method.
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    # It is the convolution of image with the kernel specified to give a gradiant along x axis. The place where the
    # filter has to applied, the method and the kernel size is determined. 1, 0 simply specifies that the filtering
    # is along x axis.
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    # It is the convolution of image with the kernel specified to give a gradiant along y axis. The place where the
    # filter has to applied, the method and the kernel size is determined. 0, 1 simply specifies that the filtering
    # is along y axis.
    canny = cv2.Canny(frame, 100, 200)
    # Applying the canny filter and specifying the source and size.
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('canny', canny)
    # Give the outputs
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()