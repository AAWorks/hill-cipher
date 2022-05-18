import numpy as np

# Simple Hill Cipher Implementation

def encrypt(toEncrypt: str, key: str):
    encryptMatrixIn = []
    for char in toEncrypt:
        encryptMatrixIn.append([ord(char)])
    print(encryptMatrixIn)
    toProcessMatrix = np.array(encryptMatrixIn)
    print(toProcessMatrix)

if __name__ == "__main__":
    encrypt("rick", "")