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

import logging
import os
import datetime

#
# A singleton logger that will be used globally by the project
# All the log files are created inside ./logs/ dir with current date
#


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                    SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(object, metaclass=SingletonType):
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger("crumbs")
        self._logger.setLevel(logging.DEBUG)

        # creating a logging format
        fmt = "[%(levelname)s] %(asctime)s :: %(filename)s:%(lineno)d -" \
            " %(funcName)s() | %(message)s"
        formatter = logging.Formatter(fmt)

        # ensuring that logs dir exist
        now = datetime.datetime.now()
        dirname = "./logs"

        if not os.path.isdir(dirname):
            os.mkdir(dirname)

        # setting handlers
        fileHandler = logging.FileHandler(
                dirname + "/log_" + now.strftime("%Y-%m-%d")+".log")
        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)


def get_logger():
    return Logger.__call__()._logger

if __name__ == "__main__":
    logger = get_logger()
    logger.debug("some debug log")
    logger.info("Hello Navi")
    logger.warning("here is a warning !!!")
