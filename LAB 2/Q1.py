str=input("Enter a string")
slist=str.split()
d=dict()
for i in slist:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
count=0
for i in d:
    count+=d[i]
print("Unique Words=",len(d))
print("Total words=",count)#can also use len(slist) directly
