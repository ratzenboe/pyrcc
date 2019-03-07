#!/usr/bin/env python

from distutils.core import setup

setup(name='pyrcc',
  version= '0.1',
  description='A python implementation of Robust Continuous Clustering',
  author='Yann Henon',
  package_data={'': ['Readme.md']},
  include_package_data=True,
  license="MIT",
  py_modules=['rcc'],
  requires = ['numpy','scipy'],
  url = 'https://github.com/yhenon/pyrcc',
  keywords = ['machine learning', 'clustering', 'RCC', 'python']
 )
