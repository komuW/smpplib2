from setuptools import setup, find_packages
import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name="smpplib2",
      version='0.1',
      url='https://github.com/komuW/smpplib2',
      description='SMPP library for python',
      packages=find_packages(),
      zip_safe=True,
      classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: MIT License',
        ],
      **extra
)
