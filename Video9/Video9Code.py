import cv2
import numpy as np
# Importing libraries
cap = cv2.VideoCapture(0)
# Using first camera to capture the video.
while (1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    kernel = np.ones((5, 5), np.uint8)
    # Explained in the previous code till here.
    erosion = cv2.erode(mask, kernel, iterations=1)
    # Erosion works on the basis that if the kernel comes across even a single 0 then the all the points within the
    # region becomes 0 as well. Due to this the width of the image reduces during erosion. This also helps to reduce
    # the background noise greatly. The source, kernel specifications and number of iterations are defined.
    dilation = cv2.dilate(mask, kernel, iterations=1)
    # Dilation works on the basis that even if there is a single 1 then thw whole region under the kernel comes 1.
    # So, in this case, the width of the iamge will increase.
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # Opening is simply erosion followed by dilation. This is actually the best method in most cases to remove noise.
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # Closing is the opposite of opening, i.e. dilation followed by erosion. If there are small disturbances in the
    # fore-image, it is useful in covering that.
    gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
    # It is the difference of dilation and erosion.
    tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
    # It is the difference of input image and opening.
    blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
    # It is the difference of closing and input image.
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()