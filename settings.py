#!/usr/bin/python3

"""
 ROBOVISION
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

###########################################################
#                                                         #
# settings/config script for various params/variables etc #
#                                                         #
###########################################################

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

#
# packet/buffer size to send each packet during file transfer
#
FILE_PKT_SIZE = 4096

#
# port for receiving files
#
FILE_RECV_PORT = 8888
