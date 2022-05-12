import cv2 as cv
import numpy as np

image_path = "images/test_palm.jpeg"
image = cv.imread(image_path)
cv.imshow(image_path, image)
cv.waitKey(1)
