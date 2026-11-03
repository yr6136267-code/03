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

# r = int(input()) // matrix total
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
# print(s)

# n = int(input()) // Diagonal sum of a matrix
# m = [list(map(int, input().split())) for i in range (n)]
# s=0
# s1=0
# for i in range (0,n):
#     s=s+m[i][i]
#     s1=s1+m[i][n-1-i]
# print(s,s1)

# r, c = map(int, input().split()) // transpose of a matrix
# m = [list(map(int, input().split())) for i in range(r)]

# for j in range(c):
#     for i in range(r):
#         print(m[i][j], end=" ")
#     print()

# r, c = map(int, input().split()) // Diagonal traversal
# m = [list(map(int, input().split())) for i in range(r)]

# for s in range(r + c - 1):
#     for i in range(r):
#         j = s - i
#         if j>=0 and j<c:
#             print(m[i][j], end=" ")
#     print()


# r, c = map(int, input().split()) // zig zag trversal
# m = [list(map(int, input().split())) for i in range(r)]
# res = []
# for s in range(r + c - 1):
#     diag = [m[i][s - i] for i in range(r) if 0 <= s - i < c]
#     if s % 2 == 0:
#         diag.reverse()
#     res += diag
# print(*res)
# n = int(input())
# i = 1
# while i<=n:
#     print(" "*(2*n-i),end="")
#     j = i
#     while j>=1:
#         print(j,end="")
#         j-=1
#     k=j
#     while k<=i:
#         print("",end="")
#         k+=1
#     print()
#     i+=1
# n = int(input())
# i = 1
# while i <= n:
#     print("  " * (n - i), end="")
#     j = i
#     while j >= 1:
#         print(j, end="")
#         if j > 1:
#             print(" ", end="")
#         j -= 1
#     print()
#     i += 1

# n = int(input()) // Square Spiral
# a = [[0]*n for i in range(n)]
# t, b, l, r = 0, n-1, 0, n-1
# num = 1

# while t <= b and l <= r:
#     for i in range(l, r+1):        
#         a[t][i] = num
#         num += 1
#     t += 1

#     for j in range(t, b+1):        
#         a[j][r] = num
#         num += 1
#     r -= 1

#     if t <= b:
#         for i in range(r, l-1, -1):  
#             a[b][i] = num
#             num += 1
#         b -= 1

#     if l <= r:
#         for j in range(b, t-1, -1):  
#             a[j][l] = num
#             num += 1
#         l += 1

# for row in a:
#     print("".join(f"{k:3}" for k in row))

n=int(input())
for i in range (1,n+1):
    for j in range (1,(2*n)+1):
        if j>i and j<=(2*n)-i:
            print(" ",end="")
        else:
            print("*",end="")
    print()
for i in range (n-1,0,-1):
    for j in range (1,(2*n)+1):
        if j>i and j<=(2*n)-i:
            print(" ",end="")
        else:
            print("*",end="")
    print()

# n = int(input())
# a = []
# for i in range(1, n + 1):
#     r = []
#     for j in range(i):
#         if j == 0 or j == i - 1:
#             r.append(1)
#         else:
#             r.append(a[j - 1] + a[j])
#     print(" ".join(str(x) for x in r))
#     a= r
