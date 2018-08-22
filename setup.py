#!/usr/bin/env python3

from setuptools import setup

setup(name='python-cli-template',
      version='0.1.0',
      description='Template of CLI application',
      author='Hibikine Kage',
      author_email='mail@hibikine.me',
      url='https://github.com/HibikineKage/python-cli-template',
      py_modules=['module_name'],
      install_requires=[],
      entry_points='''
            [console_scripts]
            module_name=cli:cli
      '''
      )
