import numpy as np
import sympy as sp
import string, itertools, random

ALPHABET = string.ascii_uppercase + "0123456789"

def clean(inputstr: str, size: int):
    diff = len(inputstr) % size
    salt = "".join([ALPHABET[x - 5] for x in range(diff)])
    return inputstr if len(inputstr) % size == 0 else inputstr + salt

def encrypt(inputstr: str, keyMatrixIn: list):
    toEncrypt=clean(inputstr.upper(), 2)

    seq = [ALPHABET.index(char) for char in toEncrypt if char.isalnum()]
    encryptMatrixIn = [seq[x::2] for x in range(2)]
    toProcessMatrix = np.array(encryptMatrixIn)
    keyMatrix = np.array(keyMatrixIn)
    result = np.matmul(keyMatrix, toProcessMatrix)
    alphali1 = [ALPHABET[int(item)] for item in np.mod(result,36)[0]]
    alphali2 = [ALPHABET[int(thing)] for thing in np.mod(result,36)[1]]
    resultlist = [x for x in itertools.chain.from_iterable(itertools.zip_longest(alphali1,alphali2)) if x]
    ans = ""
    for i in range(0, len(inputstr)):
        if toEncrypt[i].isalnum():
            letter = resultlist.pop(0)
            if inputstr[i].islower():
                ans += letter.lower()
            else:
                ans += letter
        else:
            ans += toEncrypt[i]
    return ans