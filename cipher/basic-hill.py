import numpy as np

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

if __name__ == "__main__":
    encrypt("ACT", "GYBNQKURP")