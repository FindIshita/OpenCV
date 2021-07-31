import cv2
import numpy as np
# Importing libraries
cap = cv2.VideoCapture(0)
# This is for webcam to capture the video we are about to use in the later stage. I used 0 because I am using my
# first camera.
while (1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([31, 150, 50])
    upper_red = np.array([255, 255, 180])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # Upto this point everything is same as the previous code.
    kernel = np.ones((15,15),np.float32)/225
    # np.ones creates an array of the given dimensions, in this case, 15 rows and 15 columns. Considering that we
    # multiply rows and columns and divide the whole by the asnwer (15*15 = 225 so dividing by 225)
    smoothed = cv2.filter2D(res,-1,kernel)
    gaussian_blur = cv2.GaussianBlur(res, (15, 15), 0)
    # Here in gaussian blur, the source which needs to be blurred, the size of the kernel to be used and the standard
    # deviation along x and y axis are specified.
    median_blur = cv2.medianBlur(res, 15)
    # Just the source and linear aperture size is determined. The size should be greater than 1 and odd.
    bilateral_blur = cv2.bilateralFilter(res, 15, 75, 75)
    # The source, destination, sigma color and sigma space are described.
    cv2.imshow('Original',frame)
    cv2.imshow('res', res)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('Gaussian Blurring', gaussian_blur)
    cv2.imshow('Median Blur', median_blur)
    cv2.imshow('bilateral Blur', bilateral_blur)
    # Outputs
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()