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
# command line script for opencv functions
#

import argparse
import sys
import cv2


class Opencv(object):

    def __init__(self):

        parser = argparse.ArgumentParser(description='Opencv commandline')
        parser.add_argument('command', help='Subcommand to run')

        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_help()
            exit(1)

        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def to_grayscale(self):
        try:

            parser = argparse.ArgumentParser(
                    description='Convert an image to grayscale')

            # required fields for creating a gitlab user
            parser.add_argument('--input', help='input image name/path')
            parser.add_argument('--output', help='output image name/path')

            # parse args for this command
            args = parser.parse_args(sys.argv[2:])

            # converting image to grayscale
            img = cv2.imread(args.input, 0)

            # saving grayscaled image to output file
            cv2.imwrite(args.output, img)

            print(
                "Converted '%s' to grayscale and saved in '%s'" %
                (args.input, args.output))
        except Exception as exp:
            print(
                "Got exception while converting image to grayscale: ",
                str(exp))


if __name__ == "__main__":
    Opencv()
