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

# r, c = map(int, input().split()) //Diagonal traversal
# m = [list(map(int, input().split())) for i in range(r)]

# for d in range(r + c - 1):
#     for i in range(r):
#         j = d- i
#         if j>=0 and j<c:
#             print(m[i][j], end=" ")
    
   


# r, c = map(int, input().split())// zigzag traversal
# m = [list(map(int, input().split())) for i in range(r)]

# res = [] 
# for d in range(r + c - 1):
#     diag = []
#     for i in range(r):
#         j = d - i
#         if 0 <= j < c:
#             diag.append(m[i][j])
#     if d % 2 == 0:
#         diag.reverse()
#     res += diag

# print(*res)

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

# n = int(input()) //
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

# n=int(input())
# for i in range (1,n+1):
#     for j in range (1,(2*n)+1):
#         if j>i and j<=(2*n)-i:
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()
# for i in range (n-1,0,-1):
#     for j in range (1,(2*n)+1):
#         if j>i and j<=(2*n)-i:
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()

# n = int(input())// Pascal triangle
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

# r = int(input()) 
# c = int(input())

# a = []
# b=[]
# i = 0
# while i < r:
#     row = list(map(int, input().split()))
#     a.append(row)
#     i += 1
# col=0
# while col<c:
#     temp=[]
#     r-=1
#     while r>=0:
#         temp.append(a[r][col])
#         r-=1
#     b.append(temp)
#     col+=1
# print(b)

# n, m = map(int, input().split())// codeforces 34B-4
# prices = list(map(int, input().split()))
# earn = 0
# for i in range(m):
#     if prices[i] < 0:
#         earn += -prices[i]
# print(earn)

# t = int(input())//codeforces 1360B-29
# for i in range(t):
#     n = int(input())
#     s = list(map(int, input().split()))

#     s.sort()

#     ans = s[1]-s[0]
#     for i in range(n - 1):
#         diff = s[i + 1] - s[i]
#         if diff < ans:
#             ans = diff

#     print(ans)
# A, B, C = map(int, input().split()) // 3D list sum elements

# cube = []
# for a in range(A):
#     block = []
#     for b in range(B):
#         row = list(map(int, input().split()))
#         block.append(row)
#     cube.append(block)

# total = 0
# for a in range(A):
#     for b in range(B):
#         for c in range(C):
#             total += cube[a][b][c]

# print(total)




