import re
from itertools import chain
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
from distutils.core import setup
from distutils.command.build import build
from setuptools.command.develop import develop
from setuptools.command.easy_install import easy_install
from setuptools.command.install_lib import install_lib

VERSION = '0.1.0'

setup(
    name = 'portship',
    packages = ['portship'],
    version = VERSION,
    description = 'ROSE Online asset extrator',
    author = 'Josh Junon',
    author_email = 'josh@junon.me',
    url = 'https://github.com/sevenhearts/portship',
    download_url = 'https://github.com/sevenhearts/portship/archive/{}.tar.gz'.format(VERSION),
    keywords = ['rose', 'online', 'seven', 'hearts', 'portship', 'extractor'],
    classifiers = [],
    extras_require = {
        ':sys_platform=="win32"': ['colorama']
    },
    install_requires = [
        'pgmagick'
    ]
)
