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


class Robot(Thread):


    def __init__(self, lbl):
        super().__init__()
        self.lbl = lbl

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

    def face_open(self):
        add_image_to_label(self.lbl, "./images/robot/normal.png")

    def run(self):
        while True:
            self.look_left()
            time.sleep(1)
            self.look_right()
            time.sleep(1)
            self.look_up()
            time.sleep(1)
