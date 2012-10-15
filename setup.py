#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# setup.py -
#
# Author: Paolo Olivo (paolo.olivo@inria.fr)
#
# See the file LICENSE for information on usage and redistribution of
# this file, and for a DISCLAIMER OF ALL WARRANTIES.

from distutils.core import setup

long_description = """**livedesktop** periodically sends network requests to obtain the view of a public webcam; the obtained image is written to a target file, which is periodically refreshed.

Configure your desktop wallpaper to slide show, and select the target folder in order to have the webcam view on your desktop."""

setup(
    name = "livedesktop",
    version = "0.1.0",
    py_modules = ("livedesktop", ),
    scripts = ("livedesktop", ),

    author = "Paolo Olivo",
    author_email = "olivopaolo@tiscali.it",
    url = "https://github.com/olivopaolo/livedesktop",
    description = "Bring your desktop wallpaper alive!",
    long_description = long_description,
    license = "GPLv3",
    classifiers = (
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        'Intended Audience :: End Users/Desktop',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Utilities",
        ),
)
