# Repeating Characters

For this problem, you will write a program that takes a string of characters, S, and creates a new string of characters, T, with each character repeated R times. That is, R copies of the first character of S, followed by R copies of the second character of S, and so on. Valid characters for S are the QR Code "alphanumeric" characters:

0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ$%*+-./:

Input

The first line of input contains a single integer P, ( 1 ≤ P ≤ 1000), which is the number of data sets that follow. Each data set is a single line of input consisting of the data set number N, followed by a space, followed by the repeat count R, ( 1 ≤ R ≤ 8), followed by a space, followed by the string S. The length of string S will always be at least one and no more than 20 characters. All the characters will be from the set of characters shown above.

Output

For each data set there is one line of output. It contains the data set number, N, followed by a single space which is then followed by the new string T, which is made of each character in S repeated R times.

Example Input 1 

2

3 ABC

5 /HTP

Example Output 1 

AAABBBCCC

/////HHHHHTTTTTPPPPP

Source

ICPC > Regionals > North America > Greater New York Region > 2011 Greater New York Programming Contest A

Used Algorithms:

Implementation
String
