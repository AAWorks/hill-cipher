<!-- Just to make latex readable in the dark -->

<style>
    img{
        background-color: white;
        padding-right: 5px;
        padding-top: 5px;
        padding-bottom: 5px;
    }
</style>

# About the Hill Cipher

## Matrix Multiplication

One of the most important things involved in the Hill Cipher is matrix multiplication. As a refresher:

- You need two matrixes, A and B
- Width of matrix A needs to be equal to the height of matrix B
- The resulting matrix will be the height of matrix A and the width of matrix B
- Each slot is the dot product of the corresponding row values of matrix A and column values of matrix B (if this doesn't make sense right now, just pay attention to the example I'll show y'all)

For example, given matrix A, a 2x3 matrix, and matrix B, a 3x6 matrix, shown below:

<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}1&space;&&space;2&space;&&space;3&space;\\4&space;&&space;5&space;&&space;6&space;\\\end{bmatrix}\begin{bmatrix}7&space;&&space;8&space;&&space;9&space;&&space;0&space;&&space;1&space;&&space;2&space;\\3&space;&&space;4&space;&&space;5&space;&&space;6&space;&&space;7&space;&&space;8&space;\\9&space;&&space;0&space;&&space;1&space;&&space;2&space;&&space;3&space;&&space;4&space;\\\end{bmatrix}&space;">

If you do A*B (matrix multiplication of A and B), this is the resulting matrix:

<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}1*7&space;&plus;&space;2*3&space;&plus;&space;3*9&space;&&space;1*8&space;&plus;&space;2*4&space;&plus;&space;3*0&space;&&space;1*9&space;&plus;&space;2*5&space;&plus;&space;3*1&space;&&space;1*0&space;&plus;&space;2*7&space;&plus;&space;3*3&space;&&space;1*1&space;&plus;&space;2*7&space;&plus;&space;3*3&space;&&space;1*2&space;&plus;&space;2*8&space;&plus;&space;3*4&space;\\4*7&space;&plus;&space;5*3&space;&plus;&space;6*9&space;&&space;4*8&space;&plus;&space;5*4&space;&plus;&space;6*0&space;&&space;4*9&space;&plus;&space;5*5&space;&plus;6*1&space;&&space;4*0&space;&plus;&space;5*6&space;&plus;&space;6*2&space;&&space;4*1&space;&plus;&space;5*7&space;&plus;&space;6*3&space;&&space;4*2&space;&plus;&space;5*8&space;&plus;&space;6*4&space;\\\end{bmatrix}">

<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}40&space;&&space;16&space;&&space;22&space;&&space;18&space;&&space;24&space;&&space;30&space;\\97&space;&&space;52&space;&&space;67&space;&&space;42&space;&&space;57&space;&&space;72&space;\\\end{bmatrix}">

Note that matrix multiplication is not commutative, even if the A and B have the same dimensions. This means that A and B cannot be swapped around (like in normal multiplication).

## Requirements to use the Hill Cipher (the original version)

- an alphabetical text to encode via the cipher. All letters should be in the same case for ease of use. Numbers are not allowed in the original implementaion, but we have some tricks up our sleeves...
- The matrix should have a modular inverse. If there is no modualar inverse for the matrix, then you won't be able to decode the ciphertext and the encoded text is just as useful as a md5 hash (lol!). We also have some tricks up our sleeves for this....

## Encoding text

Let the text to be encoded be ACT, and the key matrix be:

<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}6&space;&&space;24&space;&&space;21\\&space;13&space;&&space;16&space;&&space;10\\&space;20&space;&&space;17&space;&&space;15\end{bmatrix}">

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

<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}6&space;&&space;24&space;&&space;21\\&space;13&space;&&space;16&space;&&space;10\\&space;20&space;&&space;17&space;&&space;15\end{bmatrix}">

0. Find the modular inverse with the mod being 26 (which involves trying to find the inverse of the matrix, then plugging and chugging for x in the number involved * x % 26 to get the modular inverse, which is hell)

   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}6&space;&&space;24&space;&&space;1&space;\\13&space;&&space;16&space;&&space;10&space;\\20&space;&&space;17&space;&&space;15&space;\\\end{bmatrix}^{-1}(\textup{mod&space;}&space;26)&space;\equiv&space;\begin{bmatrix}8&space;&&space;5&space;&&space;10&space;\\21&space;&&space;8&space;&&space;21&space;\\21&space;&&space;12&space;&&space;8&space;\\\end{bmatrix}">

1. Put the index of all the characters of the text in a vertical matrix, from left to right. For example, POH would be placed in the vector like this:
   
   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}15\\&space;14\\&space;7\end{bmatrix}">

2. Perform matrix multiplication

   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}8&space;&&space;5&space;&&space;10&space;\\21&space;&&space;8&space;&&space;21&space;\\21&space;&&space;12&space;&&space;8&space;\\\end{bmatrix}\begin{bmatrix}15&space;\\14&space;\\7\end{bmatrix}=\begin{bmatrix}260&space;\\574&space;\\539\end{bmatrix}">

3. Do modulo 26 to the matrix

   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}260&space;\\574&space;\\539\end{bmatrix}&space;\equiv&space;\begin{bmatrix}0&space;\\2&space;\\19\end{bmatrix}(\textup{mod&space;}&space;26)">

4. Convert the matrix contents to alphabetical characters, going from top to bottom.

   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}0&space;\\2&space;\\19\end{bmatrix}\to&space;ACT">

## What about longer strings?

- Split the input string up into matrix row length sized pieces substrings and repeatedly do the encryption or decryption steps for each substring and combine at the end.

## Our Implementation

- The inital implementaion of the Hill Cipher is a mostly faithful remake (no, not the faithful the Pokemon company said with the gen 4 remakes, an actual faithful remake) of the Hill Cipher, with the same limitations of the Hill Cipher. We did take the liberty of making all chars all caps just to make our lives easier, but beyond that and the fact that the matrix row and column count must be the same length as the input string, it functions the same.
- Our Flask site implementation of the Hill Cipher preserves the capitalization of the string and allows numbers to be used and doesn't have the matrix size limitations.