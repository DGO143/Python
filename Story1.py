"""
    Minimalistic story, using mainly the commands time.sleep and print, and raw_input.
    Copyright (C) 2014 Luuk Willems

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
Storyline: All Rights Reserved by Luuk Willems.
"""

import time
time.sleep(1)
print "Mysterious Voice: \'Hello.\'"
time.sleep(2)
print "                  \'Delicious friend.\'"
time.sleep(3)
print "                                        You: \'What...\'"
time.sleep(1)
print "                                             \'What happened?\'"
time.sleep(3)
print "                  \'Hm. Maybe.\'"
time.sleep(3)
print "                                             \'Okay...?\'"
time.sleep(1.5)
print "                                             \'By the way, where are we going?\'"
time.sleep(3)
print "Where do you want to go?"
time.sleep(1)
place = raw_input("North, East, South or West? (\"n\"/\"e\"/\"s\"/\"w\")")
