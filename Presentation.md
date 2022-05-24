# About the Hill Cipher

## Encoding via the Hill Cipher

Requirements to use the Hill Cipher:

- a text to encode via the cipher
- a key matrix that is as long as the text to encode, squared

Let the text to be encoded be ACT, and the key matrix be:

6 24 1
13 16 10
20 17 15

0. Put the index of all the characters of the text in a vertical matrix, from left to right. For example, ACT would be placed in the vector like this:

0
2
19

1. Perform matrix multiplication

6 24 1      0       67
13 16 10 *  2   =   222
20 17 15    19      319

2. Do modulo 26 to the matrix

67         15
222 % 26 = 14
319        7

3. Convert the matrix contents to alphabetical characters, going from top to bottom.

15
14  => POH
7