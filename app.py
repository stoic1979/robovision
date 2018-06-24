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

import sys
import os

from PyQt5 import QtGui, QtCore, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QListWidgetItem
from PyQt5.uic import loadUi

from logger import get_logger
log = get_logger()

DIRPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))


class AppWindow(QMainWindow):
    """
    Main GUI class for application
    """

    def __init__(self):
        QWidget.__init__(self)

        # loaind ui from xml
        uic.loadUi(os.path.join(DIRPATH, 'app.ui'), self)


        # button event handlers
        self.btnOk.clicked.connect(self.ok_pressed)

    def ok_pressed(self):
        log.debug("[AppWindow] :: ok")
        self.show_msgbox("AppWindow", "Its ok")

    def show_msgbox(self, title, text):
        """
        Function for showing error/info message box
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information) 
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
	
        retval = msg.exec_()
        print("[INFO] Value of pressed message box button:", retval)

##############################################################################
#                                                                            #
#                                 MAIN                                       #
#                                                                            #
##############################################################################
if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = AppWindow()
    window.resize(1240, 820)	
    window.show()
    sys.exit(app.exec_())
