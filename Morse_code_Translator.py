import os

###Morse code dictionary
CODE = {'A': '.-',   'B': '-...',  'C': '-.-.',
        'D': '-..',  'E': '.',     'F': '..-.',
        'G': '--.',  'H': '....',  'I': '..',
        'J': '.---', 'K': '-.-',   'L': '.-..',
        'M': '--',   'N': '-.',    'O': '---',
        'P': '.--.', 'Q': '--.-',  'R': '.-.',
        'S': '...',  'T': '-',     'U': '..-',
        'V': '...-', 'W': '.--',   'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }


##make directory
path = "Output"
os.makedirs(path, exist_ok=True)

#Ask for user input
message = input("Please enter a message to translate: ").upper()

##Create out test file for message
with open("Output/Message.txt", "w") as file:
    file.write(message)


#List
l =[]

##Translate method
def translate(message):

    words = message.split()
    ##For each word
    for word in words:
        ##For each character
        for char in word:
            print(CODE[char])
            l.append(CODE[char])
            #l.append("/")
        l.append("/")
        print("\n")

##Call method
translate(message)

##Join list into a string
morsecode = " ".join(l)

print("CODE : {}".format(morsecode))

##Write morsecode to output file
with open("Output/Morsecode.txt", "w") as mfile:
    mfile.write(morsecode)