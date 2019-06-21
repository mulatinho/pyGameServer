# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Author: Alexandre Mulatinho <alex@mulatinho.net>

import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir, "security"))
import security as SEC

def test_IF_KEY_IS_CREATE():
    instance = SEC.Security()
    instance.pk_new_key()

def test_IF_KEY_IS_A_FILE():
    return 0
