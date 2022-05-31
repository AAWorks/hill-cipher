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

- You need two matrixes, called A and B
- Width of matrix A needs to be equal to the height of matrix B
- The resulting matrix will be the height of matrix A and the width of matrix B
- Each slot is the dot product of the corresponding row values of matrix A and column values of matrix B

## Encoding text

Requirements to use the Hill Cipher:

- a text to encode via the cipher
- a key matrix that is as long as the text to encode, squared

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

1. Perform matrix multiplication

   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}8&space;&&space;5&space;&&space;10&space;\\21&space;&&space;8&space;&&space;21&space;\\21&space;&&space;12&space;&&space;8&space;\\\end{bmatrix}\begin{bmatrix}15&space;\\14&space;\\7\end{bmatrix}=\begin{bmatrix}260&space;\\574&space;\\539\end{bmatrix}">

2. Do modulo 26 to the matrix

   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}260&space;\\574&space;\\539\end{bmatrix}&space;\equiv&space;\begin{bmatrix}0&space;\\2&space;\\19\end{bmatrix}(\textup{mod&space;}&space;26)">

3. Convert the matrix contents to alphabetical characters, going from top to bottom.

   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}0&space;\\2&space;\\19\end{bmatrix}\to&space;ACT">