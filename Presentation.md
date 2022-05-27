# About the Hill Cipher

## Encoding text

Requirements to use the Hill Cipher:

- a text to encode via the cipher
- a key matrix that is as long as the text to encode, squared

Let the text to be encoded be ACT, and the key matrix be:

<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}6&space;&&space;4&space;&&space;21\\&space;13&space;&&space;16&space;&&space;10\\&space;20&space;&&space;17&space;&&space;15\end{bmatrix}">

0. Put the index of all the characters of the text in a vertical matrix, from left to right. For example, ACT would be placed in the vector like this:

<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}0\\&space;2\\&space;19\end{bmatrix}">

1. Perform matrix multiplication

<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}6&space;&&space;4&space;&&space;21\\&space;13&space;&&space;16&space;&&space;10\\&space;20&space;&&space;17&space;&&space;15\end{bmatrix}*&space;\begin{bmatrix}0\\&space;2\\&space;19\end{bmatrix}&space;=&space;\begin{bmatrix}67&space;\\222&space;\\319\end{bmatrix}">

2. Do modulo 26 to the matrix

<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}67&space;\\222&space;\\319\end{bmatrix}&space;%&space;26&space;=\begin{bmatrix}15&space;\\14&space;\\7\end{bmatrix}&space;">

3. Convert the matrix contents to alphabetical characters, going from top to bottom.

<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}15&space;\\14&space;\\7\end{bmatrix}&space;\to&space;POH">

4. Profit!

## Decoding text

The steps are relatively similar to encoding, but there are some plot twists.

Let the text to be decoded be POH, and the key matrix be:

<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}6&space;&&space;4&space;&&space;21\\&space;13&space;&&space;16&space;&&space;10\\&space;20&space;&&space;17&space;&&space;15\end{bmatrix}">

0. Find the modular inverse with the mod being 26.
   0. Some initialization steps though:
      0. Make an identity matrix, like this
      1. Manipulate the original and identity matrix such that the original matrix becomes the identity matrix. Operations should apply to both the original and identity matrixes.
   This can be done through the Euclidean Algorithm
   0. Given A and B, which are two integers that we want to find the greatest common divisor of such that A < B, inputted into gcd(A,B) (this function!)
   1. If A = 0, return B and terminate
   2. If B = 0, return A and terminate
   3. Otherwise, list out A = A / B + A % B, and do gcd(B, A % B)
   4. Keep on doing this till either 1 or 2 is fulfilled. This is the real gcd(A, B)
   5. Rewrite the listed equations that have a remainder such that the remainder is isolated.
   6. Starting from the bottom of the list of rewritten equations, substitute the equation above into the bottom of the list of rewritten equations and keep it on the bottom. Remove the equation above the bottom of the equation and repeat this till the bottom equation is the one remaining.
   7. You should get an equation in the format of au + bv = d, where d is the last nonzero remainder that you got in step 4, and a and b are the original inputs into the gcd function. u and v are the other factors that we just got (not what we started out with). We can safely ignore v and u is the modular inverse. (There are some weird and insane steps that are relevant to if a is greater than b, but we won't get to that).
1. Perform matrix multiplication
2. Do modulo 26 to the matrix
3. Convert the matrix contents to alphabetical characters, going from top to bottom.