# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright (c) 2013 - 2013 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

"""
Creates translatable strings for the Frescobaldi User Manual.

This script is run standalone.

"""

from __future__ import unicode_literals

import sys
sys.path.insert(0, '..')

import simplemarkdown
import userguide.read 


class Parser(userguide.read.Parser):
    def translate(self, s):
        print '_("' + s.replace('"', '\\"') + '")'


def main():
    p = Parser()
    for name in sys.argv[1:]:
        p.parse(userguide.read.document(name)[0])

if __name__ == '__main__':
    main()
