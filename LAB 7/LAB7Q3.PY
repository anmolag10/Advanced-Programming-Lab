f= open("test.txt","r+")
txt=f.read()
lines=txt.split("\n")
n=len(lines)-1
while n>=0:
    print(lines[n])
    n-=1


