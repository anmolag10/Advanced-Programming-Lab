f= open("input.txt","r+")
txt=f.read()
lines=txt.split("\n")
print(len(lines))
cw=0
cc=0
for line in lines :
    words=line.split(" ")
    cw+=len(words)
    for word in words:
        cc+=len(word)
print(cc)
print(cw)