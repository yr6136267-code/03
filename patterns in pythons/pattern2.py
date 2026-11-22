# O E O E 
# E E E E
# O E O E
# E E E E
n=int(input())
for i in range (1,n+1):
    if i%2==0:
        for j in range(1,n+1):
            print("E",end=" ")
    else:
        for j in range(1,n+1):
            if j%2==0:
                print("E",end=" ")
            else:
                print("O",end=" ")
    print()