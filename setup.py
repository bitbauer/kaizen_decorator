#!/usr/bin/env python

from distutils.core import setup
from glob import glob

from setuptools import find_packages

setup(name='Gericht Decorator Example',
      version='1.0',
      description='Python Decorator Example for UM Kaizen Coding',
      author='bitbauer@outlook.com',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
     )
