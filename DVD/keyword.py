# WRITTEN FOR PYTHON 3

# This file uses the keyword variant of the substitution
# cipher to encode or decode a message. Simply input a keyword and some text.

import re

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abcList = tuple(abc)
onlyAZ = lambda s: re.match('^[A-z]+$', s) != None

def kwToKey(keyword: str):

    if onlyAZ(keyword):

        lastLetterIndex = abcList.index(keyword.upper()[-1])
        _abc = list(abcList[lastLetterIndex:])
        for i in abcList[:lastLetterIndex]:
            _abc.append(i)

        _kw = ""
        
        for letter in keyword.upper():
            if letter not in _kw:
                _kw = "{0}{1}".format(letter, _kw)
            else:
                raise ValueError("The keyword must not contain repeat letters")

        keyword = _kw

        for letter in keyword:
            del _abc[_abc.index(letter)]
            _abc.insert(0, letter)

        fullKey = ""
        
        for letter in _abc:
            fullKey += letter
        return fullKey

    else:
        raise ValueError("The keyword must contain only characters A-Z.")

def decode(ciphertext: str, keyword: str):

    ciphertext = ciphertext.upper().replace(" ", "")

    if onlyAZ(ciphertext):
        key = kwToKey(keyword)
        decoded = ""
        
        for letter in ciphertext:
            decoded += abc[key.index(letter)]

        return decoded

    else:
        raise ValueError("The encoded text must not contain non-Latin alphabet characters.")

def encode(plaintext: str, keyword: str):

    plaintext = plaintext.upper().replace(" ", "")

    if onlyAZ(plaintext):
        key = kwToKey(keyword)
        encoded = ""
        
        for letter in plaintext:
            encoded += key[abc.index(letter)]

        return encoded

    else:
        raise ValueError("The input text must not contain non-Latin alphabet characters.")

print("Ready to accept commands! Use kwToKey(keyword) to generate a full key from a keyword, and encode(text, keyword) or decode(text, keyword) to begin.")
