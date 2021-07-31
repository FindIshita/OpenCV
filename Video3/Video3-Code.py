import numpy as np
import cv2
# Importing python libraries
img = cv2.imread('OpenCVimg.jpg', cv2.IMREAD_COLOR)
# Reading the image by defining it's path and flag
cv2.line(img, (0, 0), (700, 800), (255, 0, 255), 40)
# This code enables us to draw a line over the image. The first part "cv2.line" states that the object that we are
# going to draw is a line. Now the "img" refers to the image read above, the next part is the starting point of line
# followed by the ending point of line. Then comes the color of the line in BGR format. At last the thickness of the
# line in pixels is defined.
cv2.rectangle(img, (250, 250), (500, 500), (0,255, 255), 40)
# This code enables us to draw a rectangle over the image. The first part "cv2.rectangle" states that the object that
# we are going to draw is a rectangle. Now the "img" refers to the image read above, the next part is the starting
# point of rectangle followed by the ending coordinates. Then comes the color of the border of the rectangle in BGR
# format. At last the thickness of the rectangle border in pixels is defined. If the value of thickness is given as
# -1 then it fills the image with border color.
cv2.circle(img, (0, 0), 80, (255, 255, 0), 40)
# This code enables us to draw a circle over the image. The first part "cv2.circle" states that the object that we
# are going to draw is a circle. Now the "img" refers to the image read above, the next part is the coordinates of
# the center of the circle followed by the radius of the circle. Then comes the color of the border of the circle in
# BGR format. At last the thickness of the circle in pixels is defined. If thickness is -1 then it fills in colour of
# the border of the circle.
pts = np.array([[100, 50], [200, 300], [200, 200], [500, 100]], np.int32)
# These are the points (in sense , the co-ordinates) of the polygon which we are making in the next step.
cv2.polylines(img, [pts], True, (0, 255, 255), 3)
# This command is used to draw any polygon. The function "cv2.polylines" is used to specify that the image we are
# trying to draw is a polygon. The next part specifies teh image "img" on which we are going to dra the image. The
# next part is the points we defined above. The "true" above signifies that the polygon is a closed one. On the
# contrary, if the value is "false" then the polygon is open (meaning in sense that the start point does not coincide
# with the end point. The next part is for color (in BGR) followed by the last parameter which is thickness of the
# edges of the polygon.
font = cv2.FONT_HERSHEY_SIMPLEX
# Specify the font.
cv2.putText(img, 'Made by - ISHITA', (400, 200), font, 2, (200, 30, 120), 6, cv2.LINE_AA)
# This is used for over-writing on an image. "cv,putText" defines that we are about to put text. "img" is the image
# on which we are about to put text. `The next part is the text we rae about to put. It is then followed by the
# co-ordinates of the bottom left of the text of the image. Next the font is specified followed by font-scale. Then
# is the color of the image and then the thickness in pixels. Finally, we specify the type of line to be used (
# optional).
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Shows the image and closes the window when required.
