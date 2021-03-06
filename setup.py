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
    name='digitick-client',
    version=version,
    description='An swagger-generated application providing an API access to digitick shopping websites',
    author='François GUÉRIN',
    author_email='fguerin@ville-tourcoing.fr',
    url='https://github.com/frague59/digitick-client',
    license='MIT',
    keywords='digitick swagger REST API',
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: POSIX :: Linux',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Utilities', ],
    install_requires=['certifi', 'urllib3', 'six'],

    # Source files
    packages=find_packages('.'),

    # Includes static files
    include_package_data=True,

)

