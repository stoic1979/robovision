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

import os

from PyQt5 import QtGui, QtCore, uic
from PyQt5.QtWidgets import QDialog, QWidget

DIRPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))


class AboutDialog(QDialog):

    def __init__(self):
        QWidget.__init__(self)

        # loaind ui from xml
        self.ui = uic.loadUi(os.path.join(DIRPATH, 'about_dialog.ui'), self)

    def display(self):
        self.ui.show()
