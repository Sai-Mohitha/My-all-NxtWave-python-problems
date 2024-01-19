n=int(input()) #reading the input

for i in range(1,n+1):
    a=int(input())
    factor=0
    for j in range(1,a+1):
        if a%j==0:
            factor+=1 
    if factor==2:
        print(a)
        break