r,c=map(int,input().split())
a=[]
for i in range(r):
    a.append(list(map(int,input().split())))

for d in range(r+c-1):
    temp=[]
    for i in range(r):
        j=d-i
        if 0<=j<c:
            temp.append(a[i][j])
    if d%2==0:
        temp.reverse()
    print(*temp,end=" ")
print()