#
# script for evaluating some image processing features of opencv
#

import cv2


class ImageTests:


    def __init__(self):
        pass


    def grayscale(self):

        print("[ImageTests] :: testing grayscale image")

        # load an color image in grayscale 
        img = cv2.imread('./samples/penguin.jpg', 0) 

        cv2.imshow('image', img)

        """
        The function waits for specified milliseconds for any keyboard event. 
        If you press any key in that time, the program continues. 
        If 0 is passed, it waits indefinitely for a key stroke. 
        """
        cv2.waitKey(0)

        # destroy all the windows we created
        cv2.destroyAllWindows()


if __name__ == "__main__":
    it = ImageTests()
    it.grayscale()
