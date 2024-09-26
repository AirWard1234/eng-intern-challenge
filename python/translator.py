# braille dictionary for all the letters
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
}

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
        else:
            # if its not a space, take the chunk and get a correlating letter from the dictionary stated above and append it to our list
            decoded_message.append(BRAILLE_DICT.get(braille_char, ''))

        # increase i by 6 each time so that we keep moving up 6 chunks
        i += 6  
    
    return ''.join(decoded_message)

def english_to_braille(text):
    # flip the braille dictionary and call it ENGLISH_DICT
    ENGLISH_DICT = {v: k for k, v in BRAILLE_DICT.items()}
    # main array for the output
    decoded_message = []
    # loop through the characters in the text
    for english_char in text:
        # detect spaces
        if english_char == " ":
            decoded_message.append('......')
        # detect uppercase letters
        elif english_char.isupper():
            # if the letter is upper case, put ".....o" and then use the ENGLISH_DICT to locate the lowercase version of the character
            decoded_message.append(".....o" + ENGLISH_DICT.get(english_char.lower(), ''))
        else:
            decoded_message.append(ENGLISH_DICT.get(english_char, ''))

    return ''.join(decoded_message)

# Examples
# 'Hello World' braille .....oo.oo..o..o..o.o.o.o.o.o.o..oo............o.ooo.oo..oo.o.ooo.o.o.o.oo.o..
text = input("")

decoded_message = braille_to_english(text)
# decoded_message = english_to_braille(text)
print(decoded_message)