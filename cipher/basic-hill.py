import numpy as np

# Simple Hill Cipher Implementation

def encrypt(toEncrypt: str, key: str):
    encryptMatrixIn = ''
    for char in toEncrypt:
        encryptMatrixIn += char + ' ; '
    toProcessMatrix = np.matrix(encryptMatrixIn)