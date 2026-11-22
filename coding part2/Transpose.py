r,c=map(int,input().split())
a=[]
b=[]
for i in range(0,c):
    b.append([0]*r)
for i in range(0,r):
    row=list(map(int,input().split()))
    a.append(row)
for i in range(0,r):
    for j in range(0,c):
        b[j][i]=a[i][j]
print("Transpose of the matrix is:")
for i in range(0,c):
    for j in range(0,r):
        print(b[i][j],end=" ")
    print()
