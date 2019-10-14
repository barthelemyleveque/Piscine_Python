import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ' ':' / '} 

i = len(sys.argv)
if (i < 2):
    sys.exit()
string = ''
for arg in sys.argv:
    if (arg != sys.argv[0]):
        string += (arg + ' ')
string = string[:-1].upper()
to_print = ''
for char in string:
    if (MORSE_CODE_DICT[char]):
        to_print += MORSE_CODE_DICT[char]
    else:
         sys.exit('ERROR')
print(to_print)