#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File name: setup.py
    Author: Luis Roberto Pereira de Paula
    Date created: 2015-11-20
    Date last modified: 2015-11-20
"""

from setuptools import setup

setup(name='PySimprocSP',
      version='0.2',
      description='Get process details in the Simproc system on the \
           website of the city of São Paulo.',
      url='http://github.com/luisrpp/python-simproc-sp',
      author='Luis Roberto Pereira de Paula',
      author_email='luisrpp@gmail.com',
      license='MIT',
      packages=['PySimprocSP'],
      install_requires=[
          'beautifulsoup4==4.4.1',
          'requests==2.8.1'
      ],
      zip_safe=False)
