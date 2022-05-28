# About the Hill Cipher

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

0. Find the modular inverse with the mod being 26.

   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}6&space;&&space;24&space;&&space;1&space;\\13&space;&&space;16&space;&&space;10&space;\\20&space;&&space;17&space;&&space;15&space;\\\end{bmatrix}^{-1}(\textup{mod&space;}&space;26)&space;\equiv&space;\begin{bmatrix}8&space;&&space;5&space;&&space;10&space;\\21&space;&&space;8&space;&&space;21&space;\\21&space;&&space;12&space;&&space;8&space;\\\end{bmatrix}">
   
1. Perform matrix multiplication

   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}8&space;&&space;5&space;&&space;10&space;\\21&space;&&space;8&space;&&space;21&space;\\21&space;&&space;12&space;&&space;8&space;\\\end{bmatrix}\begin{bmatrix}15&space;\\14&space;\\7\end{bmatrix}=\begin{bmatrix}260&space;\\574&space;\\539\end{bmatrix}">

2. Do modulo 26 to the matrix

   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}260&space;\\574&space;\\539\end{bmatrix}&space;\equiv&space;\begin{bmatrix}0&space;\\2&space;\\19\end{bmatrix}(\textup{mod&space;}&space;26)">

3. Convert the matrix contents to alphabetical characters, going from top to bottom.

   <img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}0&space;\\2&space;\\19\end{bmatrix}\to&space;ACT">