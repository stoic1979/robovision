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

from PyQt5.QtGui import QPixmap
import pyttsx3

def add_image_to_label(lbl, img_path):
    """
    Note: to add an image to a PyQt5 window/dialog, 
    we need to create a label and add an image to that label.

    Also, we can resize the label as per dimensions of image.

    """
    pixmap = QPixmap(img_path)
    lbl.setPixmap(pixmap)
 
    # optional, resize window to image size
    lbl.resize(pixmap.width(),pixmap.height())

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

