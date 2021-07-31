import cv2
import numpy as np
# Importing libraries
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# Importing the cascades
cap = cv2.VideoCapture(0)
# Using the webcam to capture the video.
while True:
    ret, img = cap.read()
    # Reading the input video.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Change from colored to grayscale.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # The face detection happens when we specify the source, scale factor and minimum neighbours.
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 255), 2)
        # This specifies that a rectamgle of above mentioned color and thickness is to drawn around the detected area.
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        # The same thing as the face is done for the eyes in above mentioned 3 steps.
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew,ey+eh), (0,255,0), 2)
            # This specifies that a rectangle of the colour and thickness has to be drawn around detected eye.
    cv2.imshow('img', img)
    # Output is shown
    k = cv2.waitKey(5) & 255
    if k == 3:
        break
cap.release()
cv2.destroyAllWindows()
