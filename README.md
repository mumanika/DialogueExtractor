# DialogueExtractor
The script allows one to extract all dialogues in a .txt file

Readme_Dialogue_Dracula
________________________

Programming language: Python 3.7.5

Author: Mukul Manikandan (mmanika@ncsu.edu)

The script takes a text file as an input and extracts all dialogues that are enclosed within ASCII "<>","<>.,"<>_,"<>..

An output file of the users choice will be created in the local directory of the script and will contain all the dialogues that conform to the above mentioned format. 

Steps to run the script: 
On the terminal, use the following command in the directory of the script: python Dialogue_Dracula.py <file_name_to_be_searched> <file_name_for_the_output>

Libraries that are used in the script: re,os,sys

Readme_Dialogue_Search_Dracula
_______________________________

Programming language: Python 3.7.5

Author: Mukul Manikandan (mmanika@ncsu.edu)

The script takes a required dialogue as an input and searches the text file for it's presence. If present, the script outputs the number and name of the chapter that the dialogue is present in.
The chapter number and the chapter name will be printed out on the terminal from where the program is invoked.

Steps to run the script: 
On the terminal, use the following command in the directory of the script: python Dialogue_Search_Dracula.py <file_name_to_be_searched> "<text_to_be_searched>"
NOTE: The text to be searched must be enclosed in double quotes.

Libraries that are used in the script: re,os,sys


