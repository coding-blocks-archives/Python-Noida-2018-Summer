import numpy as np

import cv2

import time

cap = cv2.VideoCapture(0)

count = 0

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret, img = cap.read()

    # time.sleep(1)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    faces = face_detector.detectMultiScale(gray, 2, 5)

    if len(faces) > 0:
        (x, y, w, h) = faces[0]

        face = img[y:y+h, x:x+w]

        cv2.imshow("image", face)

    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 4)




    # cv2.imwrite("images/" + str(count) + "-image.jpg", img)
    # count += 1

    cv2.waitKey(1)
