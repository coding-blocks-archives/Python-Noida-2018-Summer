import numpy as np

import cv2

import time

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, img = cap.read()

    # time.sleep(1)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    cv2.imshow("image", gray)


    # cv2.imwrite("images/" + str(count) + "-image.jpg", img)
    # count += 1

    cv2.waitKey(1)
