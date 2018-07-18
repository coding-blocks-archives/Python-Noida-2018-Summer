import numpy as np

import cv2

# img = np.zeros((400, 400, 1), np.uint8)
img = cv2.imread("anuj.jpg")

cv2.line(img, (100, 100), (200, 200), (255, 255, 255), 2)
cv2.rectangle(img, (100, 100), (200, 200), (255, 255, 255), 2)

cv2.imshow("my_image", img)

cv2.waitKey(0)








