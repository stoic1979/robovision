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
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QBasicTimer


class VideoCapture(QObject):
    """
    Class for capturing video from web camera using opencv

    It used an timer function to emit a Qt slot that contains image data.

    Class interested in processing this image will need to connect the slot.
    """

    # slot for emitting a frame captured from camera
    got_image_data_from_camera = pyqtSignal(np.ndarray)

    def __init__(self, camera_port=0, parent=None):
        super().__init__(parent)
        self.camera = cv2.VideoCapture(camera_port)
        self.timer = QBasicTimer()

    def start(self):
        self.timer.start(0, self)

    def stop(self):
        self.timer.stop()

    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            log.warning("Failed to setup timer for video capture")
            return

        read, data = self.camera.read()
        if read:
            self.got_image_data_from_camera.emit(data)
