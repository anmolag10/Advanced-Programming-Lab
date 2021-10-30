sarray=[]
l=int(input("Enter l"))
for i in range(0,l):
    ele=input("Enter String\t")
    sarray.append(ele)
print("Strings entered:  ",sarray)

count=0
for i in sarray:
    if (len(i)>2 and i[0]==i[-1]):
        count+=1
print("no of string with 1st and last same:", count)
for i in sarray:
    if(len(i)%2!=0):
        print(i)
