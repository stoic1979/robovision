#
# command line script for opencv functions
#

import argparse
import sys


class Opencv(object):

    def __init__(self):

        parser = argparse.ArgumentParser( description='Opencv commandline')
        parser.add_argument('command', help='Subcommand to run')
        
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_help()
            exit(1)

        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def to_grayscale(self):
        print ("convering to grayscale")

        parser = argparse.ArgumentParser(description='Convert an image to grayscale')

        # required fields for creating a gitlab user
        parser.add_argument('--input', help='input image name/path')
        parser.add_argument('--output', help='output image name/path')

        # parse args for this command
        args = parser.parse_args(sys.argv[2:])

        print("Converted '%s' to grayscale and saved in '%s'" % (args.input, args.output) )



if __name__ == "__main__":
    Opencv()


