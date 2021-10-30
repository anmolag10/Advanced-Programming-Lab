mat1 = []
mat2 = []
print("Enter the elements of the matrix 1")

for i in range (0,n):
    row = []
    list = input()
    row = list.strip().split(' ');
    mat1.append(row)
print("Matrix 1", mat1)
print("Enter the elements of the matrix 2")

for i in range (0,n):
    row = []
    list = input()
    row = list.strip().split(' ');
    mat2.append(row)
print("Matrix 2", mat2)




matdic1 = {}
matdic2 = {}
# Processing for matrix 1
i = 0
for row in mat1:
    k = 0
    for j in row:
        if int(j) != 0:
            matdic1[(i, k)] = j
        k += 1
    i += 1
print("Matrix Dic 1 ", matdic1)
# processing for matrix 2
i = 0
for row in mat2:
    k = 0
    for j in row:
        if int(j) != 0:
            matdic2[(i, k)] = j
        k += 1
    i += 1
print("Matrix Dic 2 ", matdic2)
matdic3={}
for i in range(0, n):
    for j in range ( 0, m ):
        if (i,j) in matdic1 and matdic2:
            matdic3[(i,j)]=int(matdic1[(i,j)])+int(matdic2[(i,j)])
        elif (i,j) in matdic1 and (i,j) not in matdic2:
                matdic3[(i,j)]=matdic1[(i,j)]
        elif (i, j) in matdic2 and (i, j) not in matdic1:
            matdic3[(i, j)] = matdic2[(i, j)]

print(matdic3)

