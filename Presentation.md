# About the Hill Cipher

## Encoding text

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

4. Profit!

## Decoding text

The steps are relatively similar to encoding, but there are some plot twists.

Let the text to be decoded be POH, and the key matrix be:

6 24 1
13 16 10
20 17 15

0. Find the modular inverse with the mod being 26.
   This can be done through the Euclidean Algorithm
   0. Given A and B, which are two integers that we want to find the greatest common divisor of, inputted into gcd(A,B) (this function!)
   1. If A = 0, return B and terminate
   2. If B = 0, return A and terminate
   3. Otherwise, let R = A % B and do gcd(B, R). This is a recursive function and will only end when either of the above cases are true
   4. 