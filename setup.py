# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='simple-blockchain',
    version='0.1.0',
    description='This is a simplified model of a blockchain, which is also the technology behind the well known crypto-currency Bitcoin.',
    long_description=readme,
    author='Aleksander Sadowski',
    author_email='aleksander.sadowski@alsado.de',
    url='https://github.com/alekssadowski95/simple-blockchain',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

