#!/usr/bin/env python

import re
import codecs
import os

# Prevent spurious errors during `python setup.py test`, a la
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html:
try:
    import multiprocessing
except ImportError:
    pass


from setuptools import setup


def read(*parts):
    return codecs.open(
        os.path.join(os.path.dirname(__file__), *parts),
        encoding='utf-8'
    ).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name='optisorl',
    version=find_version('optisorl', '__init__.py'),
    url='https://github.com/peterbe/optisorl',
    author='Peter Bengtsson',
    author_email='mail@peterbe.com',
    description="Backend plugin for sorl-thumbnail that optimizes thumbnails",
    long_description=read('README.rst'),
    packages=['optisorl'],
    license='BSD',
    include_package_data=True,
    test_suite='runtests.runtests',
    tests_require=['sorl-thumbnail', 'mock'],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
