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
# a mouth that maintains of queue of text to be spoken
#
# it has a slot to feed text to be spoken by it
#
# this text is added in a queue to be played

import time
from multiprocessing import Queue
from threading import Thread

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from utils import speak_text

from global_signals import g_emitter

from logger import get_logger
log = get_logger()


class Mouth(QObject, Thread):

    def __init__(self, parent=None):
        super().__init__(parent)

        # max capacity of mouth
        BUF_SIZE = 100
        self.queue = Queue(BUF_SIZE)

    @pyqtSlot('QString')
    def feed_text(self, text):
        log.info("Mouth fed with text: %s" % text)
        self.queue.put(text)

    def run(self):
        while True:
            if not self.queue.empty():
                text = self.queue.get()
                log.info("Mouth speaking text: %s" % text)

                # ignore empty/None texts
                if not text or not len(text):
                    continue
                speak_text(text)

                # tell face to change mouth animations to speaking
                g_emitter().emit_signal_to_set_speaking_state()

                time.sleep(.1)
            else:
                # tell face to change mouth animations to idle
                time.sleep(.2)
                g_emitter().emit_signal_to_set_idle_state()
