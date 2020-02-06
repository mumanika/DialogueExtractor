import re
import sys
from os import path

if len(sys.argv)==3:
    readFile=sys.argv[1]
    search_string = sys.argv[2]
    if not path.isfile(readFile):
        print("Given input file does not exist.")
        sys.exit(0)
    if path.isfile(sys.argv[2]):
        print("The second argument should be a search string, not a file!")
        sys.exit(0)
else:
    print("Please enter the arguments correctly.\nFor example: python dialogue.py <input file name> <output file name>")
    sys.exit(0)

with open(readFile,'r') as f:
    contents=f.read()

paragraphs = re.split(r"\n\n", contents)

#quotes=re.compile(r"[\"'\u2018\u2019\u201c\u201d]")

NotFound=False
LookupIndex=[]
for x in paragraphs:
    quotes = re.compile(r'(\".*?\")|(^\"[^"]*\')|(^\"[^"]*\.)|(^\"[^"]*--)|(^\"[^"]*_)', re.DOTALL)
    quoteMatch=quotes.finditer(x)
    for i in quoteMatch:
        if search_string.strip() in re.sub(' +', ' ', repr(i.group(0)).replace('\\n', ' ').replace('\\','').strip('\'')).lstrip('\"').rstrip('\"'):
            NotFound = True
            LookupIndex.append(paragraphs.index(x))

if not NotFound:
    print("Dialogue not found.")
else:
    print("Instance(s) of search string found in dialogues. Details below.")
    for i in LookupIndex:
        for j in range(i-1,-1,-1):
            if "chapter" in paragraphs[j].lower():
                print("Chapter number:\t",paragraphs[j].strip())
                print("Chapter name:\t",paragraphs[j+1].strip())
                break











