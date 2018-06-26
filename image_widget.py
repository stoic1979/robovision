#!/usr/bin/python3

"""
 RoboVision
 ______________

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

 Project Author/Architect: Navjot Singh <weavebytes@gmail.com>

"""

import cv2
import numpy as np
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QPainter


class ImageWidget(QWidget):
    """
    Qt Widget to show an image or a frame from video
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # image to be show in widget
        self.image = QImage()
        self._red = (0, 0, 255)
        self._width = 2
        self._min_size = (30, 30)

    def handle_image_data(self, image_data):
        self.image = self.get_qimage(image_data)
        if self.image.size() != self.size():
            self.setFixedSize(self.image.size())

        # redrawing the image
        self.update()

    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape
        bytesPerLine = 3 * width

        # composing image from image data
        image = QImage(image.data,
                       width,
                       height,
                       bytesPerLine,
                       QImage.Format_RGB888)

        image = image.rgbSwapped()
        return image

    def reset(self):
        # creating an empty image to reset/empty the widget
        self.image = QImage()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QImage()
