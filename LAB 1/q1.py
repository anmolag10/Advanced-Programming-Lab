print("Enter size of list 1")
n1=input()
n2=int(input("Enter size of list 2"))
a=[]
b=[]

for i in range(0,int(n1)):
    elem=int(input("Enter Value in 1:"))
    a.append(elem)
for i in range(0,n2):
    elem=int(input("Enter Value in 2:"))
    b.append(elem)

c=[]
for i in a:
    if i%2!=0:
        c.append(i)
for i in b:
    if i%2==0:
        c.append(i)
print("List A:",a)
print("List B:",b)
print("List C:",c)

