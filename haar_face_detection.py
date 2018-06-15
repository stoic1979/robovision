#
# face detection from an image using Haar cascade classifier
#

import numpy as np
import cv2 as cv

# lets us pretrained cascade classifiers of opencv for face and eyes detection

# train/initialize face classifier
face_cascade = cv.CascadeClassifier('./cascades/haarcascades_cuda/haarcascade_frontalface_default.xml')

# train/initialize eye classifier
eye_cascade = cv.CascadeClassifier('./cascades/haarcascades_cuda/haarcascade_eye.xml')

# reading the image
img = cv.imread('./samples/people.jpg')

# HAAR cascade will need a grayscaled image to detect faces and eyes
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# lets find faces in the image and get their positions
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:

    # drawing rect for face
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # drawing rects for eyes
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# showing image
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
