import re
import sys
from os import path

if len(sys.argv)==3:
    readFile=sys.argv[1]
    if not path.isfile(readFile):
        print("Given input file does not exist.")
        sys.exit(0)
    writeFile=sys.argv[2]
else:
    print("Please enter the arguments correctly.\nFor example: python dialogue.py <input file name> <output file name>")
    sys.exit(0)


with open(readFile,'r') as f:
    contents=f.read()

paragraphs = re.split(r"\n\n", contents)
# quotes=re.compile(r"[\"'\u2018\u2019\u201c\u201d]")

with open(writeFile,'w+') as f:
    pass

for x in paragraphs:
    quotes = re.compile(r'(\".*?\")|(^\"[^"]*\')|(^\"[^"]*\.)|(^\"[^"]*--)|(^\"[^"]*_)', re.DOTALL)
    quoteMatch=quotes.finditer(x)
    with open(writeFile,'a+') as f:
        for i in quoteMatch:
            text=re.sub(' +', ' ', repr(i.group(0)).replace('\\n', ' ').replace('\\','').strip('\''))
            f.write(text+"\n")








