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
import cv2
import numpy as np

from PyQt5 import QtGui, QtCore, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (
        QApplication, QWidget, QMenu, QMainWindow, QMessageBox, QFileDialog,
        QListWidgetItem, QSystemTrayIcon, QStyle, QAction, qApp)
from PyQt5.uic import loadUi

from about_dialog import AboutDialog
from prefs_dialog import PrefsDialog
from video_capture import VideoCapture
from image_widget import ImageWidget

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
        self.btnStartCaptureForVideoAnalysis.clicked.connect(
                self.start_capture_for_video_analysis)
        self.btnStopCaptureForVideoAnalysis.clicked.connect(
                self.stop_capture_for_video_analysis)

        self.btnChooseClassifierXML.clicked.connect(self.choose_classifier_file)

        self.setup_tray_menu()

        # add camera ids
        for i in range(0, 11):
            self.cboxCameraIds.addItem(str(i))
            self.cboxCameraIds1.addItem(str(i))

        # setting up handlers for menubar actions
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(qApp.quit)
        self.actionPreferences.triggered.connect(self.show_preferences)

        self.img_widget = ImageWidget()
        self.hlayoutVideoAnalysis.addWidget(self.img_widget)

        self.vid_capture = VideoCapture()
        self.vid_capture.got_image_data_from_camera.connect(
                self.process_image_data_from_camera)

        self.highlight_faces = self.chkHighlightFaces.isChecked()
        self.chkHighlightFaces.stateChanged.connect(self.highlight_faces_checkbox_changed)

    def highlight_faces_checkbox_changed(self):
        if self.chkHighlightFaces.isChecked():
            print ("yes")
        else:
            print ("no")

    def choose_classifier_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        log.info("chose classfier xml file: %s" % fname[0])
        self.teClassifierXML.setText(fname[0])

    def start_capture_for_video_analysis(self):
        log.debug("start video capture")
        self.vid_capture.start()

    def stop_capture_for_video_analysis(self):
        log.debug("start video capture")
        self.vid_capture.stop()
        self.img_widget.reset()

    def detect_face_in_image_data(self, image_data):
        """
        function detects faces in image data,
        draws rectangle for faces in image data,
        and returns this updated image data with highlighted face/s
        """
        self._red = (0, 0, 255)
        self._width = 2
        self._min_size = (30, 30)

        # haarclassifiers work better in black and white
        gray_image = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.equalizeHist(gray_image)

        # path to Haar face classfier's xml file
        face_cascade_xml = './cascades/haarcascades_cuda/haarcascade_frontalface_default.xml'
        self.classifier = cv2.CascadeClassifier(face_cascade_xml)
        faces = self.classifier.detectMultiScale(gray_image,
                                                 scaleFactor=1.3,
                                                 minNeighbors=4,
                                                 flags=cv2.CASCADE_SCALE_IMAGE,
                                                 minSize=self._min_size)

        for (x, y, w, h) in faces:
            cv2.rectangle(image_data,
                          (x, y),
                          (x+w, y+h),
                          self._red,
                          self._width)

        return image_data

    def process_image_data_from_camera(self, image_data):
        if self.chkHighlightFaces.isChecked():
            image_data = self.detect_face_in_image_data(image_data)
        self.img_widget.handle_image_data(image_data)

    def about(self):
        ad = AboutDialog()
        ad.display()

    def show_preferences(self):
        print("preferences")
        pd = PrefsDialog()
        pd.display()

    def setup_tray_menu(self):

        # setting up QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(
                self.style().standardIcon(QStyle.SP_ComputerIcon))

        # tray actions
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)

        # action handlers
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)

        # tray menu
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "RoboVision",
            "RoboVision was minimized to Tray",
            QSystemTrayIcon.Information,
            2000
        )

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
