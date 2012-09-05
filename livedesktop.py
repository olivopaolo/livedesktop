#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# livedesktop.py -
#
# Author: Paolo Olivo (paolo.olivo@inria.fr)
#
# 'alivedesktop' periodically sends network requests to obtain the
# view of a public webcam; the obtained image is written to a target
# file, which is periodically refreshed.
#
# Configure your desktop wallpaper to slide show, and select the
# target folder in order to have the webcam view on your desktop.

import logging
import os.path
import sys

from PyQt4 import QtCore, QtNetwork

filepath = os.path.join(os.path.expanduser("~"),
                        "Downloads",
                        "desktopslideshow",
                        "pontneuf.jpg")
# url = QtCore.QUrl("http://www.vieuxlille.com/webcam/pontneuf.jpg")
# url = QtCore.QUrl("http://95.240.230.122:8251/record/current.jpg")
url = QtCore.QUrl("http://www.rumegiesmeteo.fr/WEBCAM/Photo001.jpg")

def sendRequest():
    """Send network request."""
    netmanager.get(QtNetwork.QNetworkRequest(url));

def handleReply(reply):
    """Write entire reply to the target file."""
    fd = open(filepath, "wb", 0)
    fd.write(reply.readAll())
    reply.close()
    fd.close()
    logging.info("Image refreshed.")

def timeout():
    sendRequest()

app = QtCore.QCoreApplication(sys.argv)
netmanager = QtNetwork.QNetworkAccessManager(finished=handleReply)
# Send first request
sendRequest()
# Active timer
timer = QtCore.QTimer(timeout=timeout)
timer.start(60000)

sys.exit(app.exec_())
