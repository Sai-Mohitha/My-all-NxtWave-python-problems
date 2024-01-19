n=int(input())

for i in reversed(range(1,n+1)):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        if i==n or i==j or j==1:
            print("*",end=" ")
        else:
            print("  ",end="")
    print()        