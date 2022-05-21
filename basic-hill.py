import numpy as np
import sympy as sp

# Simple Hill Cipher Implementation

def encrypt(toEncrypt: str, key: str):
    toEncrypt = toEncrypt.upper()
    key = key.upper()
    if len(key) != len(toEncrypt) ** 2:
        print("Key length is not string to encrypt length squared!")
        return
    elif len(toEncrypt) == 0:
        print("No key inputted")
    encryptMatrixIn = []
    for char in toEncrypt:
        encryptMatrixIn.append([ord(char) - 65])
    print(encryptMatrixIn)
    toProcessMatrix = np.array(encryptMatrixIn)
    print(toProcessMatrix)
    keyMatrixIn = [[]]
    for char in key:
        if len(keyMatrixIn[-1]) == 3:
            keyMatrixIn.append([])
        keyMatrixIn[-1].append(ord(char) - 65)
    print(keyMatrixIn)
    keyMatrix = np.array(keyMatrixIn)
    print(keyMatrix)
    result = np.matmul(keyMatrix, toProcessMatrix)
    print(result)
    result = np.mod(result, 26)
    print(result) # can use result = "".join([string.ascii_lowercase[int(item[0])] for item in np.mod(result, 26)])

def decrypt(toDecrypt: str, key: str):
    toDecrypt = toDecrypt.upper()
    key = key.upper()
    if len(key) != len(toDecrypt) ** 2:
        print("Key length is not string to encrypt length squared!")
        return
    elif len(toDecrypt) == 0:
        print("No key inputted")
    encryptMatrixIn = []
    for char in toDecrypt:
        encryptMatrixIn.append([ord(char) - 65])
    print(encryptMatrixIn)
    toProcessMatrix = np.array(encryptMatrixIn)
    print(toProcessMatrix)
    keyMatrixIn = [[]]
    for char in key:
        if len(keyMatrixIn[-1]) == 3:
            keyMatrixIn.append([])
        keyMatrixIn[-1].append(ord(char) - 65)
    sympyMatrix = sp.Matrix(keyMatrixIn)
    sympyMatrix = sympyMatrix.inv_mod(26)
    print(np.array(sympyMatrix.tolist()))
    

if __name__ == "__main__":
    # encrypt("ACT", "GYBNQKURP")
    decrypt("ACT", "GYBNQKURP")