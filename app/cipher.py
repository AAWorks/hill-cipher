import numpy as np
from sympy import Matrix
import string, itertools

ALPHABET = string.ascii_uppercase + "0123456789"

def clean(inputstr: str, size: int):
    return inputstr if len(inputstr) % size == 0 else inputstr + 'Z'

def encrypt(inputstr: str, keyMatrixIn: list, decoding: bool):
    instr = "".join([char for char in inputstr.upper() if char.isalnum()])
    toEncrypt=clean(instr.upper(), 2)

    seq = [ALPHABET.index(char) for char in toEncrypt if char.isalnum()]
    encryptMatrixIn = [seq[x::2] for x in range(2)]
    toProcessMatrix = np.array(encryptMatrixIn)
    keyMatrix = np.array(keyMatrixIn)

    try:
        _ = matInvMod(keyMatrix, 36)
    except:
        return "The inputted matrix has no modular inverse. Due to this, decryption is impossible and encryption is useless."

    result = np.matmul(keyMatrix, toProcessMatrix)
    alphali1 = [ALPHABET[int(item)] for item in np.mod(result,36)[0]]
    alphali2 = [ALPHABET[int(thing)] for thing in np.mod(result,36)[1]]
    resultlist = [x for x in itertools.chain.from_iterable(itertools.zip_longest(alphali1,alphali2)) if x]
    ans = ""

    for i in range(0, len(inputstr)):
        if inputstr[i].isalnum():
            letter = resultlist.pop(0)
            if inputstr[i].islower():
                ans += letter.lower()
            else:
                ans += letter
        else:
            ans += inputstr[i]
    if resultlist:
        ans += resultlist.pop(0)
    if decoding and ans[-1] == 'Z':
        ans = ans[:-1]
    return ans

def matInvMod (vmnp, mod):
    vmsym = Matrix(vmnp)
    vmsymInv = vmsym.inv_mod(mod)
    vmnpInv = np.array(vmsymInv)
    return vmnpInv

def decrypt(inputstr: str, keyMatrixIn: list, decoding: bool):
    keyMatrixIn = np.array(keyMatrixIn)
    keyMatrix = matInvMod(keyMatrixIn, 36)
    return encrypt(inputstr, keyMatrix, decoding)

#print(encrypt("Hill Clinton", [[-3,5],[1,0]]))