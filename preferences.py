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

from configparser import ConfigParser


class Preferences:

    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read("./preferences.ini")

    def load_default_preferences(self):
        """
        load default preference if preferences.ini file not found
        """
        pass

    def set_nickname(self, nickname):
        self.parser.set('General', 'Nickname', nickname)

    def get_nickname(self):
        return self.parser.get('General', 'Nickname')


if __name__ == '__main__':
    prefs = Preferences()
    prefs.set_nickname("Navi")
    print("Nickname: ", prefs.get_nickname())
