f= open("input.txt","r+")
txt=f.read()
txt.strip()
words=txt.split(" ")
dic={}
for word in words:
    if(dic.get(word)):
        dic[word]=int(dic[word])+1
    else:
        dic[word]=1
print(dic)