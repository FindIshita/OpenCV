import numpy as np
import cv2

cap = cv2.VideoCapture('people-walking.crdownload')
# We import a video for this purpose. Alternatively. the webcam can also be used.
fgbg = cv2.createBackgroundSubtractorMOG2()
# It is a gaussian mixture based algo for background subtraction.
while (1):
    ret, frame = cap.read()
    # reading the frame
    fgmask = fgbg.apply(frame)
    # Applying background subtraction.
    cv2.imshow('fgmask', frame)
    cv2.imshow('frame', fgmask)
    # Outputs
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()