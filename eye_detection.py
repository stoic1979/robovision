#
# eye detection from a live video
#

import numpy as np
import cv2 as cv


class EyeDetector:

    def __init__(self, face_cascade_xml, eye_cascade_xml):

        # lets us pretrained cascade classifiers of opencv for face and eyes detection

        # train/initialize face classifier
        self.face_cascade = cv.CascadeClassifier(face_cascade_xml)

        # train/initialize eye classifier
        self.eye_cascade = cv.CascadeClassifier(eye_cascade_xml)

        # reading data from webcam
        # for internal webcam on laptop use 0
        # for external webcam on laptop/PC use 1
        cap = cv.VideoCapture(0)

        while True:

            ret, img = cap.read()

            self.process_image(img)

            # wait for key for 10 mscs, or continue
            k = cv.waitKey(10) & 0xff

            # if 'esc' pressed, terminate
            if k == 27:
                break

        cap.release()
        cv.destroyAllWindows()

    def process_image(self, img):
        """
        this function detects eyes in a given image,
        and draws an outline rectangle across eyes
        """
        # HAAR cascade will need a grayscaled image to detect faces and eyes
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # lets find faces in the image and get their positions
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:

            # define roi for eyes detection,ideally, we should detect
            # eyes within the rectangular bounds of a face
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            # drawing rects for eyes
            eyes = self.eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

        # showing image
        cv.imshow('Haar Face Detection', img)

if __name__ == "__main__":
    # path to Haar face classfier's xml file
    face_cascade_xml = './cascades/haarcascades_cuda/haarcascade_frontalface_default.xml'

    # path to Haar eye classfier's xml file
    eye_cascade_xml = './cascades/haarcascades_cuda/haarcascade_eye.xml'

    # run the eye detector with given classfiers
    ed = EyeDetector(face_cascade_xml, eye_cascade_xml)
