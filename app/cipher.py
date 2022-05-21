import numpy as np
import sympy as sp
import string

ALPHABET = string.ascii_uppercase + "0123456789"

def encrypt(toEncrypt: str, key: str):
    encryptMatrixIn = []
    for char in toEncrypt:
        encryptMatrixIn.append(ALPHABET.index(char))
    toProcessMatrix = np.array(encryptMatrixIn)
    keyMatrixIn = [[]]
    for char in key:
        if len(keyMatrixIn[-1]) == 3:
            keyMatrixIn.append([])
        keyMatrixIn[-1].append(ALPHABET.index(char))
    keyMatrix = np.array(keyMatrixIn)
    result = np.matmul(keyMatrix, toProcessMatrix)
    ans = "".join([ALPHABET[int(item)] for item in np.mod(result, 36)])
    return ans

print(encrypt("J4ck_4nd_J1ll_w3N7_up_7H3_H1Ll", "GYBNQKURP"))