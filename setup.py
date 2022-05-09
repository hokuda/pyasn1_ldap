#!/usr/bin/env python
import os
import sys
from setuptools import setup, Command

classifiers = """\
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Information Technology
Intended Audience :: System Administrators
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Topic :: System :: Monitoring
Topic :: System :: Networking :: Monitoring
Topic :: Software Development :: Libraries :: Python Modules
Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP
"""


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()


params = {
    'name': 'pyasn1_ldap',
    'version': open('pyasn1_ldap/__init__.py').read().split('\'')[1],
    'description': 'LDAP protocol module',
    'long_description': long_description,
    'author': 'Hisanobu Okuda',
    'url': 'https://github.com/hokuda/pyasn1_ldap',
    'platforms': ['any'],
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    'classifiers': [x for x in classifiers.split('\n') if x],
    'license': 'LICENSE',
    'packages': ['pyasn1_ldap'],
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    'install_requires': ['pyasn1>=0.4.6,<0.6.0'],
}


setup(**params)
