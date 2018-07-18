import numpy as np

import cv2

import time

cap = cv2.VideoCapture(0)

count = 0

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


eyes_detector = cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    ret, img = cap.read()

    # time.sleep(1)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    faces = face_detector.detectMultiScale(gray, 2, 5)

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 4)

        gray_face = gray[y:y + h, x:x + w]

        eyes = eyes_detector.detectMultiScale(gray_face, 2, 5)

        for (ex, ey, ew, eh) in eyes :
            cv2.rectangle(img, ( x + ex, y + ey), ( x + ex + ew, y + ey + eh), (0, 255, 0), 4)

    cv2.imshow("image", img)



    # cv2.imwrite("images/" + str(count) + "-image.jpg", img)
    # count += 1

    cv2.waitKey(1)
