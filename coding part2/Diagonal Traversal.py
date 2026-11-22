# Diagonal Traversal
r,c=map(int,input().split())
a=[]
for i in range(r):
    a.append(list(map(int,input().split())))
for d in range(r+c-1):
    for i in range(r):
        j=d-i
        if j>=0 and j<c:
            print(a[i][j],end=" ")
    print()