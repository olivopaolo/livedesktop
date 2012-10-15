#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# livedesktop.py -
#
# Author: Paolo Olivo (olivopaolo@tiscali.it)
#
# See the file LICENSE for information on usage and redistribution of
# this file, and for a DISCLAIMER OF ALL WARRANTIES.

"""livedesktop periodically sends network requests to obtain the
view of a public webcam; then the image is written to a target
file, which is periodically refreshed.

Configure your desktop wallpaper to slide show, and select the
target folder in order to have the webcam view on your desktop.

URL examples:
- http://www.vieuxlille.com/webcam/pontneuf.jpg
- http://95.240.230.122:8251/record/current.jpg
- http://www.rumegiesmeteo.fr/WEBCAM/Photo001.jpg

"""

PROG = "livedesktop.py"
DEFAULT_FILENAME = "livedesktop"

import argparse
import imghdr
import logging
import os
import os.path
import sys
import time

if sys.version<'3':
    from urllib import urlopen
else:
    from urllib.request import urlopen

# Init arguments parser
parser = argparse.ArgumentParser(
    prog=PROG, description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("url", metavar="URL", help="image's URL")
parser.add_argument("target", metavar="TARGET", nargs="?",
                    default=os.getcwd(),
                    help="target directory or file (default: ./)")
parser.add_argument("-l", dest="logging_level", default="INFO",
                    metavar="LEVEL", help="set logging level")
parser.add_argument("-f", dest="freq", default=1.0, type=float,
                    help="set the refresh frequence (default: 1Hz)")

# Parse arguments
args = parser.parse_args()
logging.basicConfig(level=logging.getLevelName(args.logging_level))
if args.freq==0:
    print("%s: error: argument -f: invalid value: 0"%PROG)
    import sys ; sys.exit(-1)

if os.path.isdir(args.target):
    logging.info("Using default filename: %s", DEFAULT_FILENAME)
    dirpath = args.target
    filebasename = DEFAULT_FILENAME
else:
    dirpath, filebasename = os.path.split(args.target)

# Infinite loop
while True:
    try:
        response = urlopen(args.url)
        image = response.read()
        response.close()
        ext = imghdr.what(None, h=image)
        if ext is not None:
            filepath = os.path.join(dirpath, "%s.%s"%(filebasename, ext))
            fd = open(filepath, "wb", 0)
            fd.write(image)
            fd.close()
            logging.debug("Image refreshed.")
        else:
            logging.warning("Cannot detect image type.")
    except Exception as err:
        logging.warning(err)
    time.sleep(60/args.freq)
