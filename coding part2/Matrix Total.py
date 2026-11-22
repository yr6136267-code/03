r,c=map(int,input().split())
a=[]
s=0
for i in range(0,r):
    row=list(map(int,input().split()))
    a.append(row)
for i in range(0,r):
    j=0
    for j in range(0,c):
        s+=a[i][j]
print(s)