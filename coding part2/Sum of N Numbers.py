# Sum of N Numbers
# Input: 5 / 10 / 20 / 30 / 40 / 50      Output: 150
n=int(input())
s=0
for i in range(1,n+1):
    a=int(input())
    s+=a
print("Sum of N Numbers is:",s)
