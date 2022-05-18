import numpy as np

# Simple Hill Cipher Implementation

def encrypt(toEncrypt: str, key: str):
    if len(key) != len(toEncrypt) ** 2:
        print("Key length is not string to encrypt length squared!")
        return
    elif len(toEncrypt) == 0:
        print("No key inputted")
    encryptMatrixIn = []
    for char in toEncrypt:
        encryptMatrixIn.append([ord(char)])
    print(encryptMatrixIn)
    toProcessMatrix = np.array(encryptMatrixIn)
    print(toProcessMatrix)

if __name__ == "__main__":
    encrypt("rick", "")