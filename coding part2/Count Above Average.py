# Count Above Average
n=int(input())
a=list(map(int,input().split()))
s=0
avg=0
c=0
for i in range(0,len(a)):
    s+=a[i]
avg=s/n
for i in range (0,len(a)):
    if a[i]>avg:
        c+=1
print(f"Numbers above average are: {c}")