n = int(input("Input N:"))
m = int(input("Input M:"))
flag=1
for i in range (n,m+1):
    for j in range( 2, i+1):
        if i%j==0:
            flag=0
            break
        else:
    if flag == 1 :
        print(i,end=" ")
