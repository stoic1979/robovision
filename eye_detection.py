#
# eye detection from a live video
#

import numpy as np
import cv2 as cv

# lets us pretrained cascade classifiers of opencv for face and eyes detection

# train/initialize face classifier
face_cascade = cv.CascadeClassifier('./cascades/haarcascades_cuda/haarcascade_frontalface_default.xml')

# train/initialize eye classifier
eye_cascade = cv.CascadeClassifier('./cascades/haarcascades_cuda/haarcascade_eye.xml')

# reading data from webcam
# for internal webcam on laptop use 0
# for external webcam on laptop/PC use 1
cap = cv.VideoCapture(0)

while True:

    ret, img = cap.read()

    # HAAR cascade will need a grayscaled image to detect faces and eyes
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # lets find faces in the image and get their positions
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:

        # define roi for eyes detection,ideally, we should detect
        # eyes within the rectangular bounds of a face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # drawing rects for eyes
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # showing image
    cv.imshow('Haar Face Detection', img)

    # wait for key for 10 mscs, or continue
    k = cv.waitKey(10) & 0xff

    # if 'esc' pressed, terminate
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
