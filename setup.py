"""Packaging script for python-scpi"""
import os
import subprocess

import setuptools

GIT_VERSION = 'UNKNOWN'
try:
    GIT_VERSION = subprocess.check_output(['git', 'rev-parse', '--verify', '--short', 'HEAD']).decode('ascii').strip()
except subprocess.CalledProcessError:
    pass

setuptools.setup(
    name='scpi',
    version=os.getenv('PACKAGE_VERSION', '2.1.0+git.%s' % GIT_VERSION),
    author='Eero "rambo" af Heurlin',
    author_email='rambo@iki.fi',
    packages=['scpi'],
    license='GNU LGPL',
    long_description_content_type='text/markdown',
    description='Implement SCPI in pure Python',
    install_requires=["pyserial", "async-timeout"],
    url='https://github.com/rambo/python-scpi',
    classifiers=(
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2) ",
    ),
)
