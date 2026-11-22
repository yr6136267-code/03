r,c=map(int,input().split())
a=[]
for i in range(0,r):
    row=list(map(int,input().split()))
    a.append(row)
s=0
s1=0
for i in range(0,r):
    for j in range(0,c):
        if i==j:
            s+=a[i][j]
        if i+j==r-1:
            s1+=a[i][j]
print("Main diagonal sum is:",s)
print("Anti-diagonal sum is:",s1)