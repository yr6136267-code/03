# n=int(input()) // SUM OF n NUMBERS
# s=0
# for i in range (1,n+1):
#     a=int(input())
#     s+=a
# print(s)

# a=list(map(int,input().split())) // MAX & MIN
# max=a[0]
# min=a[0]
# for i in range (1,len(a)):
#     if max < a[i]:
#         max=a[i]
#     if min > a[i]:
#         min=a[i]
# print("Max:",max,"Min:",min)

# a=int(input()) // GCD 
# b=int(input())
# g=1
# i=1
# while i<=min(a,b):
#     if a%i==0 and b%i==0:
#         g=i
#     i+=1
# print(g)

# n=int(input()) // COUNT ABOVE AVERAGE
# a=list(map(int,input().split()))
# s=0 
# c=0
# for i in range(0,len(a)):
#     s+=a[i]
# avg=s/n
# for i in range (0,len(a)):
#     if a[i]>avg:
#         c+=1
# print(c)

# r = int(input()) // MATRIX TOTAL
# c = int(input())

# a = []
# i = 0
# while i < r:
#     row = list(map(int, input().split()))
#     a.append(row)
#     i += 1

# s = 0
# i = 0
# while i < r:
#     j = 0
#     while j < c:
#         s += a[i][j]
#         j += 1
#     i += 1

n = int(input())
m = [list(map(int, input().split())) for i in range (n)]
s=0
s1=0
for i in range (0,n):
    s=s+m[i][i]
    s1=s1+m[i][n-1-i]
print(s,s1)

