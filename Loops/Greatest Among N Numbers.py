n=int(input())
a=int(input())
b=a
for i in range(n-1):
    num=int(input())
    if (num>b):
        b=num 
print(b)     