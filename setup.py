# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import os
from distutils.core import setup
from setuptools import find_packages

# Loads the version from package
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from digitick_client import __version__ as version

setup(
    name='django-buttons',
    version=version,
    description='An application providing a API access to digitick shopping websites',
    author='François GUÉRIN',
    author_email='fguerin@ville-tourcoing.fr',
    url='https://github.com/frague59/digitick_client',
    license='MIT',
    keywords=['digitick', 'swagger',],
    classifiers=['Development Status :: 4 - Beta',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 ],
    install_requires=['certifi', 'urllib3', 'six'],

    # Source files
    packages=find_packages('.'),

    # Includes static files
    include_package_data=True,

)

