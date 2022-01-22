# Name Frequency
background:
Each year, the government puts out a list of the 10,000 most common names for babies and their frequency. The problem with this list is that some of the names can be spelled in a number of ways, for example Jacob and Yaacov are actually the same name, however they will be listed separately.

The software checks duplicates of names and returns the true frequency of each name.
The software gets two files one file of names and their frequency and another file of pairs of similar names, it reads the files and prints to a new file the real list of names and their frequency without duplicates.
The software has a single file written in Python and run by it.

Running example:

First file- names and their frequency
[frequency.txt](https://github.com/ayala6521/HomeTest/files/7919091/frequency.txt)

Jacob:15

Yaccov:12

Yaakov:3

Miriam:2

Miryam:2

Shira:22


Second File- pairs of similar names
[pairs.txt](https://github.com/ayala6521/HomeTest/files/7919092/pairs.txt)

Jacob,Yaakov

Yaccov,Yaakov

Miriam,Miryam



The final file we got- File of names and their frecuency without duplicates
[final_frequency.txt](https://github.com/ayala6521/HomeTest/files/7919093/final_frequency.txt)

Jacob,Yaakov,Yaccov:30

Miriam,Miryam:4

Shira:22




Instructions for the exercise to run well and without errors:
1. In the "frequency" file, write the name, punctuation and frequency without spaces, you have to go down a line between names --> name:frequency
2. In the "pairs" file, write the names of the pairs with a comma that separates the 2 names and without spaces between them, you have to go down a line between pairs --> name,name
3. Please pay-attention that the file names will be as follows:
   The file with the names and frequencies will be read "frequency.txt"
   The file of pairs of similar names will be read "pairs.txt"
   The final file in which the names and frequencies will be printed will be read "final_frequency.txt"
