#!/usr/bin/env python3
#
# This file is part of Script of Scripts (sos), a workflow system
# for the execution of commands and scripts in different languages.
# Please visit https://github.com/vatlab/SOS for more information.
#
# Copyright (C) 2016 Bo Peng (bpeng@mdanderson.org)

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
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys

__all__ = ['__version__', 'SOS_FULL_VERSION']

_py_ver = sys.version_info
if _py_ver.major == 2 or (_py_ver.major == 3 and (_py_ver.minor, _py_ver.micro) < (6, 0)):
    raise SystemError(
        f'SOS requires Python 3.6 or higher. Please upgrade your Python {_py_ver.major}.{_py_ver.minor}.{_py_ver.micro}.')


# version of the SoS language
__sos_version__ = '1.0'
# version of the sos command
__version__ = '0.9.10.9'
__py_version__ = f'{_py_ver.major}.{_py_ver.minor}.{_py_ver.micro}'

#
SOS_FULL_VERSION= f'{__version__} for Python {_py_ver.major}.{_py_ver.minor}.{_py_ver.micro}'
SOS_COPYRIGHT = f'''SoS {__version__} : Copyright (c) 2016 Bo Peng'''
SOS_CONTACT = '''Please visit http://github.com/vatlab/SoS for more information.'''



