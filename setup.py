# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MAS-API',
    version='0.1.0',
    description='Python HTTP Client API for Butter MAS platform',
    long_description=readme,
    author='Benny Megidish',
    author_email='bennymegk@gmail.com',
    url='https://github.com/benymeg/MAS-API',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
