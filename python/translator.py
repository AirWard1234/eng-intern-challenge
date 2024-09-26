# braille dictionaries for all the characters
BRAILLE_DICT = {
    "o.....": "a", 
    "o.o...": "b",
    "oo....": "c",
    "oo.o..": "d",
    "o..o..": "e",
    "ooo...": "f",
    "oooo..": "g",
    "o.oo..": "h",
    ".oo...": "i",
    ".ooo..": "j",
    "o...o.": "k",
    "o.o.o.": "l",
    "oo..o.": "m",
    "oo.oo.": "n",
    "o..oo.": "o",
    "ooo.o.": "p",
    "ooooo.": "q",
    "o.ooo.": "r",
    ".oo.o.": "s",
    ".oooo.": "t",
    "o...oo": "u",
    "o.o.oo": "v",
    ".ooo.o": "w",
    "oo..oo": "x",
    "oo.ooo": "y",
    "o..ooo": "z",
    "..oo.o": ".",
    "..o...": ",",
    "..o.oo": "?",
    "..ooo.": "!",
    "..oo..": ":",
    "..o.o.": ";",
    "....oo": "-",
    ".o..o.": "/",
    ".oo..o": "<",
    "o..oo.": ">",
    "o.o..o": "(",
    ".o.oo.": ")",

}
BRAILLE_NUM_DICT = {
    "o.....": "1", 
    "o.o...": "2",
    "oo....": "3",
    "oo.o..": "4",
    "o..o..": "5",
    "ooo...": "6",
    "oooo..": "7",
    "o.oo..": "8",
    ".oo...": "9",
    ".ooo..": "0",
}

# flip the braille dictionaries for English purposes
ENGLISH_DICT = {v: k for k, v in BRAILLE_DICT.items()}
ENGLISH_NUM_DICT = {v: k for k, v in BRAILLE_NUM_DICT.items()}

def braille_to_english(text):
    # empty list for the decoded words
    decoded_message = []
    # set i = 0 to be used as a way to get 6 characters at a time
    i = 0
    
    while i < len(text):
        # get 6 characters at a time by taking the i (which is 0 at first) to the i + 6th char (this would initially be 6)s
        braille_char = text[i:i+6]
        
        # if any chunk of 6 characters is "......", add a space to the decoded_message list
        if braille_char == "......":
            decoded_message.append(' ')
        # check if the chunk contains an uppercase indicator
        elif braille_char == ".....o":
            # find the next chunk
            braille_char = text[i+6: i+12]
            # append what's found in the dictionary for the next chunk, but make it uppercase
            decoded_message.append((BRAILLE_DICT.get(braille_char, '')).upper())
            # move forward by a chunk so that we don't get repeating characters
            i+=6
        # detect if the chunk is numbers
        elif braille_char == ".o.ooo":
            braille_char = text[i+6: i+12]
            decoded_message.append((BRAILLE_NUM_DICT.get(braille_char, '')))
            i+=6
        # detect if the chunk is a decimal
        elif braille_char == ".o...o":
            braille_char = text[i+6: i+12]
            decoded_message.append("."+ (BRAILLE_NUM_DICT.get(braille_char, '')))
            i+=6
        else:
            # if its not a space, take the chunk and get a correlating letter from the dictionary stated above and append it to our list
            decoded_message.append(BRAILLE_DICT.get(braille_char, ''))

        # increase i by 6 each time so that we keep moving up 6 chunks
        i += 6  
    
    return ''.join(decoded_message)

def english_to_braille(text):
    # main array for the output
    decoded_message = []
    # loop through the characters in the text
    i = 0
    while i < len(text):
        english_char = text[i]
        # detect spaces
        if english_char == " ":
            decoded_message.append('......')
        # detect uppercase letters
        elif english_char.isupper():
            # if the letter is upper case, put ".....o" and then use the ENGLISH_DICT to locate the lowercase version of the character
            decoded_message.append(".....o" + ENGLISH_DICT.get(english_char.lower(), ''))
        #  detect if the character is a number
        elif english_char.isdigit():
            decoded_message.append(".o.ooo" + ENGLISH_NUM_DICT.get(english_char, ''))
        # detect if the character is a decimal
        elif english_char == ".":
            if i + 1 < len(text) and text[i + 1].isdigit():
                decoded_message.append(".o...o" + ENGLISH_NUM_DICT.get(text[i], ''))
                i+=1
                if i < len(text):
                    decoded_message.append(ENGLISH_NUM_DICT.get(text[i], ''))
            else:
                decoded_message.append("..oo.o")
        else:
            decoded_message.append(ENGLISH_DICT.get(english_char, ''))

        i+=1

    return ''.join(decoded_message)

# ask user to input as text
text = input("")

# check if the first 3 letters are either o or . , this is to make sure the computer doesnt detect a English word that starts with an o to be braille. (I don't believe theres any word that starts with 3 'o's)
if text[0] == "o" and (text[1] == "o" or ".") and (text[2] == "o" or "."):
    decoded_message = braille_to_english(text)
# or, if the first letter is in the alphabet or is a digit, turn it from English to braille
elif text[0].isalpha() or text[0].isdigit():
    decoded_message = english_to_braille(text)
else:
    decoded_message = braille_to_english(text)

print(decoded_message)