from PIL import Image
from variables import *

def letter(y,c):
    if y is "H":
        paper.paste(H,(c,10),H)
        c=c+200
    elif y is "O":
        paper.paste(O,(c,10),O)
        c=c+200
    elif y is "L":
        paper.paste(L,(c,10),L)
        c=c+200
    elif y is "A":
        paper.paste(A,(c,10),A)
        c=c+200

sentence = input("Entrer sentence: ")
sentence.upper()
splitSentence=sentence.split(" ")
print(splitSentence)

for x in splitSentence:
    c=0
    for y in x:
        letter(y,c)
        

paper.show()




paper.show()