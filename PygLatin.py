"""
PygLatin Translator by "Locke" or "ArrowHead" (DGO143).

http://pastebin.com/u/DGO143

ASCII ART XD

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
def first_is_vowel():
    rest = word[1:]
    print rest + first + "ay"
#Welcome text:
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