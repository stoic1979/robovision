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

#
# an ear to continuously hear for sounds and make decisions
#

import time
from multiprocessing import Queue
from threading import Thread

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from utils import speak_text

from global_signals import g_emitter

import speech_recognition as sr

from logger import get_logger
log = get_logger()


class Ear(QObject, Thread):

    def __init__(self, parent=None):
        super().__init__(parent)


    def get_audio(self):
        """
        get audio from the microphone. 
        the SpeechRecognition package is used to automatically stop listening when the user stops speaking. 

        function returns the raw binary audio string (PCM)
        """
        l = sr.Microphone.list_microphone_names()
        log.debug(l)
        
        r = sr.Recognizer()

        di = l.index("default")

        with sr.Microphone(device_index=di) as source:
        #with sr.Microphone() as source:
            log.debug("listening for audio from microphone")
            #r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            log.debug("listening done")

        # convert audio to raw_data (PCM)
        raw_audio = audio.get_raw_data()

        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)

        return text

    def monitor_sounds(self):
        #TODO check audio sounds and make decisions
        pass

    def run(self):
        """
        thread function to continuously 
        """
        while True:
            monitor_sounds()
