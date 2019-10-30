# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

environment = dict()
with open("butter/mas/environment.py") as f:
    exec(f.read(), environment)

with open('README.md', encoding="utf8") as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

# install_requires = list()
# with open('requirements.txt', 'r', encoding='utf-8') as f:
#     for line in f.readlines():
#         install_requires.append(line.split("=")[0].strip("<~>"))

setup(
    name=environment['app_name'],
    version=environment['__version__'],
    description='Python Client API for Butter MAS platform',
    long_description_content_type='text/markdown',
    long_description=readme,
    author='Benny Megidish',
    author_email='bennymegk@gmail.com',
    url='https://github.com/bennymeg/Butter.MAS.PythonAPI',
    install_requires=['requests', 'packaging'],
    #license=license,
    license='Apache-2.0',
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
)

''' how to deploy '''
# python setup.py sdist bdist_wheel
# python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# pip install --index-url https://test.pypi.org/simple/ --no-deps butter.mas-api

# python -m twine upload dist/*
# pip install -U butter.mas-api

''' how to generate and serve documentation '''
# cd sphinx
# ./serve
# update tree.json file if a new file was added (the first file on the list is the default one)