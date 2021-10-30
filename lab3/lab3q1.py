def mult(l):
    prod=1
    for i in l:
        prod=prod*i
n=int(input("Enter the length of the list"))
list1=[]
for i in n:
    list1.append(i)
mult(list1)