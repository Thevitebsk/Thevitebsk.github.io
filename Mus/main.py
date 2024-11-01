c=lambda point,chr:f"ce[{point}]=={chr}"
Logo="""|    |
|\  /|
|(--)| |  | /--
|    | |  | \-\\
|    | \--/ --/
Go to https://thevitebsk.github.io/Mus/doc.html for help"""
print(Logo)
while 1:
    ce=input(">>> ");p=0
    while len(ce)>p:
        if c(p,"p") and c(p+1,"!"):
            p+=2
            while ce[p]!=")":print(ce[p],end="");p+=1
            print()
