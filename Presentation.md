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

         <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}6&space;&&space;4&space;&&space;21&space;\\13&space;&&space;16&space;&&space;10&space;\\20&space;&&space;17&space;&&space;15&space;\\\end{bmatrix}\begin{bmatrix}1&space;&&space;0&space;&&space;0&space;\\0&space;&&space;1&space;&&space;0&space;\\0&space;&&space;0&space;&&space;1&space;\\\end{bmatrix}&space;">

      1. Manipulate the original and identity matrix such that the original matrix becomes the identity matrix. Operations should apply to both the original and identity matrixes.

         <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}1&space;&&space;\frac{2}{3}&space;&&space;\frac{7}{2}&space;\\13&space;&&space;16&space;&&space;10&space;\\20&space;&&space;17&space;&&space;15&space;\\\end{bmatrix}\begin{bmatrix}\frac{1}{6}&space;&&space;0&space;&&space;0&space;\\0&space;&&space;1&space;&&space;0&space;\\0&space;&&space;0&space;&&space;1&space;\\\end{bmatrix}&space;">
         <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}1&space;&&space;\frac{2}{3}&space;&&space;\frac{7}{2}&space;\\0&space;&&space;\frac{22}{3}&space;&&space;-\frac{71}{2}&space;\\20&space;&&space;17&space;&&space;15&space;\\\end{bmatrix}\begin{bmatrix}\frac{1}{6}&space;&&space;0&space;&&space;0&space;\\-\frac{13}{6}&space;&&space;1&space;&&space;0&space;\\0&space;&&space;0&space;&&space;1&space;\\\end{bmatrix}&space;">
         <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}1&space;&&space;\frac{2}{3}&space;&&space;\frac{7}{2}&space;\\0&space;&&space;\frac{22}{3}&space;&&space;-\frac{71}{2}&space;\\0&space;&&space;\frac{11}{3}&space;&&space;-55&space;\\\end{bmatrix}\begin{bmatrix}\frac{1}{6}&space;&&space;0&space;&&space;0&space;\\-\frac{13}{6}&space;&&space;1&space;&&space;0&space;\\-\frac{10}{3}&space;&&space;0&space;&&space;1&space;\\\end{bmatrix}&space;">
         <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}1&space;&&space;\frac{2}{3}&space;&&space;\frac{7}{2}&space;\\0&space;&&space;1&space;&&space;-\frac{213}{44}&space;\\0&space;&&space;\frac{11}{3}&space;&&space;-55&space;\\\end{bmatrix}\begin{bmatrix}\frac{1}{6}&space;&&space;0&space;&&space;0&space;\\-\frac{13}{44}&space;&&space;\frac{3}{22}&space;&&space;0&space;\\-\frac{10}{3}&space;&&space;0&space;&&space;1&space;\\\end{bmatrix}&space;">
         <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}1&space;&&space;0&space;&&space;\frac{74}{11}&space;\\0&space;&&space;1&space;&&space;-\frac{213}{44}&space;\\0&space;&&space;\frac{11}{3}&space;&&space;-55&space;\\\end{bmatrix}\begin{bmatrix}\frac{4}{11}&space;&&space;-\frac{1}{11}&space;&&space;0&space;\\-\frac{13}{44}&space;&&space;\frac{3}{22}&space;&&space;0&space;\\-\frac{10}{3}&space;&&space;0&space;&&space;1&space;\\\end{bmatrix}&space;">
         <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}1&space;&&space;0&space;&&space;\frac{74}{11}&space;\\0&space;&&space;1&space;&&space;-\frac{213}{44}&space;\\0&space;&&space;0&space;&&space;-\frac{149}{4}&space;\\\end{bmatrix}\begin{bmatrix}\frac{4}{11}&space;&&space;-\frac{1}{11}&space;&&space;0&space;\\-\frac{13}{44}&space;&&space;\frac{3}{22}&space;&&space;0&space;\\-\frac{9}{4}&space;&&space;-\frac{1}{2}&space;&&space;1&space;\\\end{bmatrix}&space;">
         <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}1&space;&&space;0&space;&&space;\frac{74}{11}&space;\\0&space;&&space;1&space;&&space;-\frac{213}{44}&space;\\0&space;&&space;0&space;&&space;1&space;\\\end{bmatrix}\begin{bmatrix}\frac{4}{11}&space;&&space;-\frac{1}{11}&space;&&space;0&space;\\-\frac{13}{44}&space;&&space;\frac{3}{22}&space;&&space;0&space;\\\frac{9}{149}&space;&&space;\frac{2}{149}&space;&&space;-\frac{4}{149}&space;\\\end{bmatrix}&space;">
         <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}1&space;&&space;0&space;&&space;0&space;\\0&space;&&space;1&space;&&space;-\frac{213}{44}&space;\\0&space;&&space;0&space;&&space;1&space;\\\end{bmatrix}\begin{bmatrix}-\frac{70}{1639}&space;&&space;-\frac{27}{149}&space;&&space;\frac{296}{1639}&space;\\-\frac{13}{44}&space;&&space;\frac{3}{22}&space;&&space;0&space;\\\frac{9}{149}&space;&&space;\frac{2}{149}&space;&&space;-\frac{4}{149}&space;\\\end{bmatrix}&space;">
         <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}1&space;&&space;0&space;&&space;0&space;\\0&space;&&space;1&space;&&space;0&space;\\0&space;&&space;0&space;&&space;1&space;\\\end{bmatrix}\begin{bmatrix}-\frac{70}{1639}&space;&&space;-\frac{27}{149}&space;&&space;\frac{296}{1639}&space;\\-\frac{5}{1639}&space;&&space;\frac{30}{149}&space;&&space;-\frac{213}{1639}&space;\\\frac{9}{149}&space;&&space;\frac{2}{149}&space;&&space;-\frac{4}{149}&space;\\\end{bmatrix}&space;">

   This can be done through the Euclidean Algorithm
   1. Given A and B, which are two integers that we want to find the greatest common divisor of such that A < B, inputted into gcd(A,B) (this function!)
   2. If A = 0, return B and terminate
   3. If B = 0, return A and terminate
   4. Otherwise, list out A = A / B + A % B, and do gcd(B, A % B)
   5. Keep on doing this till either 1 or 2 is fulfilled. This is the real gcd(A, B)
   6. Rewrite the listed equations that have a remainder such that the remainder is isolated.
   7. Starting from the bottom of the list of rewritten equations, substitute the equation above into the bottom of the list of rewritten equations and keep it on the bottom. Remove the equation above the bottom of the equation and repeat this till the bottom equation is the one remaining.
   8. You should get an equation in the format of au + bv = d, where d is the last nonzero remainder that you got in step 4, and a and b are the original inputs into the gcd function. u and v are the other factors that we just got (not what we started out with). We can safely ignore v and u is the modular inverse. (There are some weird and insane steps that are relevant to if a is greater than b, but we won't get to that).
1. Perform matrix multiplication
2. Do modulo 26 to the matrix
3. Convert the matrix contents to alphabetical characters, going from top to bottom.