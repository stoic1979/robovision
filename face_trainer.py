#
# a trainer for faces, inorder to identify faces with names/labels
#
# reference
# https://www.youtube.com/watch?v=PmZ29Vta7Vc
#

import os
import numpy as np
from PIL import Image
import cv2 as cv
import pickle

from local_settings import FACE_IMAGES_DATASET_DIR

class FaceTrainer:

    def __init__(self, face_cascade_xml):

        face_cascade = cv.CascadeClassifier(face_cascade_xml)
        recognizer = cv.face.LBPHFaceRecognizer_create() 

        y_labels = []
        x_train = []
        cur_id = 0
        label_ids = {}

        # fetching images from dataset for training
        for root, dirs, files in os.walk(FACE_IMAGES_DATASET_DIR):
            for file in files:
                if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                    full_path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "-").lower()

                    if not label in label_ids:
                        label_ids[label] = cur_id
                        cur_id += 1

                    img_id = label_ids[label]
                    print (label, img_id, full_path)

                    #y_labels.append(label)
                    #x_train.append(full_path)

                    # convert image to grayscale
                    pil_image = Image.open(full_path).convert("L")

                    # convery grayscale image to numpy array
                    image_array = np.array(pil_image, "uint8")
                    #print(image_array)

                    faces = face_cascade.detectMultiScale(image_array, 1.3, 5)


                    for (x,y,w,h) in faces:
                        # define roi for eyes detection,ideally, we should detect
                        # eyes within the rectangular bounds of a face
                        roi = image_array[y:y+h, x:x+w]
                        x_train.append(roi)
                        y_labels.append(img_id)

        #print (y_labels)
        #print (x_train)
        print (label_ids)

        # save trained labels
        with open("dataset/face_trainer_labels.pickle", 'wb') as f:
            pickle.dump(label_ids, f)


        recognizer.train(x_train, np.array(y_labels))
        recognizer.save("dataset/face_trainer.yml")

if __name__ == "__main__":
    # path to Haar face classfier's xml file
    face_cascade_xml = './cascades/haarcascades_cuda/haarcascade_frontalface_default.xml'

    ft = FaceTrainer(face_cascade_xml)
