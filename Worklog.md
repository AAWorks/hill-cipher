# DevLog
Maniacal Refrigerators | Alejandro Alonso and Andy Lin <br>
Cybersecurity <br>
2022-05

---
Sample Entry: firstL -- DATE -- CONTENT\n ( e.g.: topherM -- 1999-12-31 )
<br><br>
Begin Devlog:<br><br>
alejandroA -- 2022-05-18 -- Initial repo setup
<br><br>
linAndy -- 2022-05-18 -- Initial repo setup
<br><br>
linAndy -- 2022-05-19 -- Begin work on the actual Hill Cipher code, with the matrix operations. Experimented with different libraries in Python for this, as handcoding the matrix operations isn't it
<br><br>
alejandroA -- 2022-05-19 -- Setup basic flask app for overseeing site, add information to the homepage
<br><br>
linAndy -- 2022-05-20 -- Some error handling for the input cases, made inputs more consistent and easier to deal with, experiment with more libraries. Tried to connect two libraries together, because neither could pull their weight on their own. Added a list of pip packages to install, which could be used with pip -r
<br><br>
alejandroA -- 2022-05-20 -- Added input fields for encode and decode on the machine page (plain/cipher text and key matrix).
<br><br>
alejandroA -- 2022-05-21 -- Cleaned up encrypt() function and added it to the in-app cipher.py file. Integrated with site.
<br><br>
alejandroA -- 2022-05-22 -- Decrypt() written and integrated with site. Site is functional within specific params. 
<br><br>
alejandroA -- 2022-05-23 -- Encrypt and decrypt work well with most functions, added in error handling. Will fix odd lengths tomorrow.
<br><br>
linAndy -- 2022-05-23 -- Added encryption instructions to the presentation md.
<br><br>
alejandroA -- 2022-05-24 -- Fixed issue with odd lengths and the modular inverse of the matrices. Homework.md works.
<br><br>
linAndy -- 2022-05-24 -- Added decryption information to the presentation md.
<br><br>
alejandroA -- 2022-05-25 -- Added in better error handling, data sanitizing, padding and decryption of said padding.
<br><br>
linAndy -- 2022-05-25 -- Tried to read up on modular inverse and tried to make it easy to teach on the pea sized brains of second semester seniors.
<br><br>
alejandroA -- 2022-05-26 -- Homework.md is done. Added to devlog.
<br><br>
linAndy -- 2022-05-26 -- More hair-ripping reading of modular inverse. However, I had some issues parsing out the instructions and trying to figure it out myself
<br><br>
alejandroA -- 2022-05-27 -- Added to and formatted worklog. Formatted HW file.
<br><br>
linAndy -- 2022-05-27 -- Decided to remove the inverse mod, because that would take a crapton of time we don't have and I don't think even Mr. Jaishankar would be willing to teach it in 15 minutes lol. Added some info on matrix multiplication, but not finished yet.
<br><br>
linAndy -- 2022-05-30 -- Tested out the flask site to see if there were any issues with navigations and such and fixed a navigation issue. Fixed an issue where a header gave inherently incorrect information for the capabilities of the site. Split off readme into more sections (about requirements and some edge cases). Added an implementation section. Some resoruce prepping for me if I have time for teaching the inefficient method of finding modular inverse.
<br><br>
alejandroA -- 2022-05-30 -- Added resources.
<br><br>

## Resources
Inverse Modular Matrices - [Stack Overflow](https://stackoverflow.com/questions/4287721/easiest-way-to-perform-modular-matrix-inversion-with-python)<br>
General Background - [Wikipedia](https://en.wikipedia.org/wiki/Hill_cipher)<br>
Specific Method Implementation - [dcode](https://www.dcode.fr/hill-cipher)<br>
Background for Creator - [historyoflinearalgebra](http://historyoflinearalgebra.weebly.com/lester-s-hill-jdr.html)<br>
Modular Inverse - [mathworld](https://mathworld.wolfram.com/ModularInverse.html)<br>
Modular Inverse - [youtube](https://www.youtube.com/watch?v=Rd2-EmS26uw)
Matrix Multiplication Calculator - [reshish](https://matrix.reshish.com/multiplication.php)
Matrix Inverse Calculator - [reshish](https://matrix.reshish.com/inverse.php)
