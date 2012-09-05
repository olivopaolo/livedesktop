#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# livedesktop.py -
#
# Author: Paolo Olivo (olivopaolo@tiscali.it)
#
# See the file LICENSE for information on usage and redistribution of
# this file, and for a DISCLAIMER OF ALL WARRANTIES.

"""livedesktop periodically sends network requests to obtain the
view of a public webcam; the obtained image is written to a target
file, which is periodically refreshed.

Configure your desktop wallpaper to slide show, and select the
target folder in order to have the webcam view on your desktop.

"""

import imghdr
import logging
import os.path
import time
import urllib.request

dirname = os.path.join(os.path.expanduser("~"), "Downloads", "livedesktop")
filebasename = "livedesktop"

# url = "http://www.vieuxlille.com/webcam/pontneuf.jpg"
# url = "http://95.240.230.122:8251/record/current.jpg"
url = "http://www.rumegiesmeteo.fr/WEBCAM/Photo001.jpg"

while True:
    response = urllib.request.urlopen(url)
    image = response.read()
    response.close()
    ext = imghdr.what(None, h=image)
    filepath = os.path.join(dirname, "%s.%s"%(filebasename, ext))
    fd = open(filepath, "wb", 0)
    fd.write(image)
    fd.close()
    logging.debug("Image refreshed.")
    time.sleep(60)
