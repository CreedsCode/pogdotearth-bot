# This experiment to try to detect grass will be done in a few steps.
# 3. yea idk i just work here
import cv2 as cv
import numpy as np

image_path = f"images/hands/FQ8yoKhWYAMx5Ho.jpg"
image = cv.imread(image_path)
cv.imwrite("tmp.png", image)

image = cv.imread(image_path)

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
gaussian = cv.GaussianBlur(hsv,(7, 7), 0)

# lower_range = np.array([42,100,100])
# upper_range = np.array([106,100,100])
# mask = cv.inRange(gaussian, lower_range, upper_range)

mask = cv.inRange(hsv, (36, 25, 25), (70, 255,255))

cv.imshow('Original Image', hsv)
cv.imshow('Mask', mask) 
cv.imshow('Gaussian', gaussian)

# cv.waitKey(50000)
cv.destroyAllWindows()