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
# a global sigleton signal emitter that can be used by any module
# 
# For example, any module can feed text to mouth to speak, by emitting
# an signal. Mouth enqueues the text to be spoken.
#
# Usage:
# g_emitter().emit_signal_to_feed_mouth("hello navi")
#

from PyQt5.QtCore import QObject, pyqtSignal
from singleton import SingletonType


class GlobalSignals(QObject):

    feed_mouth = pyqtSignal('QString')
    set_speaking_state = pyqtSignal()
    set_idle_state = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def emit_signal_to_feed_mouth(self, text):
        self.feed_mouth.emit(text)

    def emit_signal_to_set_speaking_state(self):
        self.set_speaking_state.emit()

    def emit_signal_to_set_idle_state(self):
        self.set_idle_state.emit()



class GlobalSignalEmitter(object, metaclass=SingletonType):
    """
    singleton class/wrapper to hold global signals to be emitted
    """

    _global_signals = None

    def __init__(self):
        self._global_signals = GlobalSignals()


def g_emitter():
    """
    function to return singleton instance of global signal emitter
    """
    return GlobalSignalEmitter.__call__()._global_signals
