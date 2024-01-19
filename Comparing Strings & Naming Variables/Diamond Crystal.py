n=int(input())

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i):
        if j==0 :
            print("/",end="")
        elif j==2*i-1:
            print("\\",end="")
        else:
            print(" ",end="")
    print()    
for i in reversed(range(1,n+1)):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i):
        if j==0 :
            print("\\",end="")
        elif j==2*i-1:
            print("/",end="")
        else:
            print(" ",end="")
    print()    

     