import numpy as np
import cv2
# Importing libraries
cap = cv2.VideoCapture(0)
# Using first webcam to capture the video
while (True):
    ret, frame = cap.read()
    # Reading the input.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Converting to grayscale.
    cv2.imshow('frame', gray)
    # Displaying the output.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()