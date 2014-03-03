"""
This is the PygLatin Translator by "Locke \ ArrowHead" (DGO143).

 The PygLatin Translator tranlates a word to Pig Latin. It is based on a tutorial that can be found at www.codeacademy.com
    Copyright (C) 2014  Luuk Willems

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
    
http://github.com/DGO143

ASCII ART INCOMING

AAAAA RRRRR RRRRR OOOOO W  W  W
A   A R   R R   R O   O W  W  W
AAAAA RRRRR RRRRR O   O W  W  W
AAAAA R R   R R   O   O W  W  W
A   A R  R  R  R  O   O W W W W
A   A R   R R   R OOOOO WW   WW

H   H EEEEE AAAAA DDDD
H   H E     A   A D   D
HHHHH EEEEE AAAAA D   D
HHHHH E     A   A D   D
H   H E     A   A D   D
H   H EEEEE A   A DDDD
  ____________
 /   ------/| \    
(        /  |  )
(       /   |  )
(     /        )
(    /         )
(  /           )      
 \/___________/

V 0.0.1.2
!!! Python 2.7 !!!

"""
import time
def first_is_vowel():
    rest = word[1:]
    print rest + first + "ay"
#Welcome text:
print "PygLatin Translator Copyright (C) 2014  Luuk Willems
print
print "   This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'."
print "   This is free software, and you are welcome to redistribute it"
print "   under certain conditions; type `show c' for details."
print " NOTE: `show w' and `show c' don't work!"
print 
time.sleep(1)
print "Welcome to the English to Pig Latin translator!"
#Asking for the word that's to be translated, storing it in the variable "original".
original = raw_input("Enter word to be translated:")
#Making sure the "original" statement isn't empty...
print "checking if not empty..."
if len(original) > 0:
    print original + " is not empty, checking if it consists solely of alphabetical characters (letters)..."
    #Making sure "original" is only alphabetical characters...
    if original.isalpha():
        print original + " consists of only alphabetical characters! Now let\'s translate it..."
        print original + "..."
        #Making "original" lowercase and storing it in the new var "word"
        word = original.lower()
        #Storing the first letter of "word" in the new var "first"
        first = word[0]
        if first == "a":
            first_is_vowel()
        elif first == "e":
            first_is_vowel()
        elif first == "u":
            first_is_vowel()
        elif first == "i":
            first_is_vowel()
        elif first == "o":
            first_is_vowel()            
        else:
            print word + "ay"     
    else:
        print "Oops, looks like " + original + " has some numerical or otherwise non-alphabetical chars in it. Weirdo."
else:
    print "You didn\'t enter anything? Weirdo."
