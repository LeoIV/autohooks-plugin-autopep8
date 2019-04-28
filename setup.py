# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

from pkg_resources import safe_version
from setuptools import find_namespace_packages

VERSION = (0, 0, 2, 'alpha')


def get_version():
    str_version = '.'.join([str(v) for v in VERSION])
    return safe_version(str_version)


with open('README.md', 'r') as f:
    long_description = f.read()  # pylint: disable=invalid-name

setup(
    name='autohooks-plugin-autopep8',
    version=get_version(),
    author='Leonard Papenmeier',
    author_email='leonard.papenmeier@posteo.de',
    description='Autohooks plugin for code formatting via autopep8',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LeoIV/autohooks-plugin-autopep8',
    packages=find_namespace_packages(include=['autohooks.*']),
    python_requires='>=3.6',
    install_requires=['autohooks>=1.1', 'autopep8'],
    classifiers=[
        # Full list: https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Version Control :: Git',
    ],
)
