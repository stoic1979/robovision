#!/usr/bin/python3

"""
 PyLanMessenger
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


import time
from threading import Thread

from utils import add_image_to_label

from random import randint

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from logger import get_logger
log = get_logger()


class Robot(QObject, Thread):
    """
    robot can have states IDLE and SPEAKING,
    depending upon state the facial images changes
    """

    @pyqtSlot()
    def set_idle_state(self):
        self.become_idle()

    @pyqtSlot()
    def set_speaking_state(self):
        self.start_speaking()

    def __init__(self, lbl, parent=None):
        super().__init__(parent)
        self.lbl = lbl

        self.idle_actions = {
                "0": self.face_normal,
                "1": self.look_left,
                "2": self.look_right,
                "3": self.look_up,
                "4": self.look_down
                }

        self.speaking_actions = {
                "0": self.face_normal,
                "1": self.mouth_open
                }

        #self.start_speaking()
        self.become_idle()

        log.debug("robot created")

    def become_idle(self):
        self.state = "IDLE"

    def start_speaking(self):
        self.state = "SPEAKING"

    def look_left(self):
        add_image_to_label(self.lbl, "./images/robot/look_left.png")

    def look_right(self):
        add_image_to_label(self.lbl, "./images/robot/look_right.png")

    def look_down(self):
        add_image_to_label(self.lbl, "./images/robot/look_down.png")

    def look_up(self):
        add_image_to_label(self.lbl, "./images/robot/look_up.png")

    def face_normal(self):
        add_image_to_label(self.lbl, "./images/robot/normal.png")

    def mouth_open(self):
        add_image_to_label(self.lbl, "./images/robot/mouth_open.png")

    def set_idle_face_img(self):
        s = str(randint(0, 2))
        try:
            self.idle_actions[s]()
        except Exception as exp:
            log.warning("robot idle state action failed")
            log.warning("with exception: %s" % str(exp))

    def set_speaking_face_img(self):
        s = str(randint(0, 1))
        try:
            self.speaking_actions[s]()
        except Exception as exp:
            log.warning("robot speaking state action failed")
            log.warning("with exception: %s" % str(exp))

    def run(self):
        while True:
            if self.state == "IDLE":
                self.set_idle_face_img()
                time.sleep(randint(1, 4))
                continue

            if self.state == "SPEAKING":
                self.mouth_open()
                time.sleep(1)
                self.face_normal()
                time.sleep(1)
                continue
