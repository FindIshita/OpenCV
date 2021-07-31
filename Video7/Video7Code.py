import cv2
import numpy as np
# Importing libraries
cap = cv2.VideoCapture(0)
# This is for webcam to capture the video we are about to use in the later stage. I used 0 because I am using my
# first camera.
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # This simply converts the BGR color to HSV color.
    lower_red = np.array([150,150,0])
    upper_red = np.array([255,255,255])
    # Setting the threshold of the color red in HSV (first value represents the hue, second represents the saturation
    # and third shows the value)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # The mask in made.
    res = cv2.bitwise_and(frame, frame, mask = mask)
    # Now as the black region has a value 0 so anything which is multiplied (every value except the threshold) will
    # become 0 pixels too, in that sense , black.
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    # Outputs
    k = cv2.waitKey(5) & 255
    if k == 27 :
        break
cv2.destroyAllWindows()
cap.release()
