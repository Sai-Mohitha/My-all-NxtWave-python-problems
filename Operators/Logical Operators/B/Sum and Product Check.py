a=int(input())
b=int(input())

c=len(str(a+b))
d=len(str(a*b))  

if (c<3 and d<3):
    print(True)
else:
    print(False)