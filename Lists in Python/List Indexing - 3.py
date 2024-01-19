n=int(input())
t=int(input())

s=[]
for i in range(n):
    a=int(input())
    s+=[a]
#print(s)
for j in range(t):
    b=int(input())
    index=s[b]
    print(index)
    