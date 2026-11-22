# Row Sums and Column Sums
r,c=map(int,input().split())  
a=[]
rsum=[] 
csum=[] 
for i in range(0,r):
    row=list(map(int,input().split()))
    a.append(row)
for i in range(0,r):
    s=0
    s1=0
    j=0
    for j in range(0,c):
        s+=a[i][j]
        s1+=a[j][i]
    rsum.append(s)
    csum.append(s1)
print("Row sums are:",*rsum)
print("Column sums are:",*csum)
