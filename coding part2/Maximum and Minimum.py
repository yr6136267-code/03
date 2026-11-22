# Maximum and Minimum
n=list(map(int,input().split()))
max=n[0]
min=n[0]
for i in range(0,len(n)):
    if n[i]>max:
        max=n[i]
    if n[i]<min:
        min=n[i]
print("Maximum number is:",max)
print("Minimum number is:",min)