s=int(input())
n=int(input())

for i in range(1,n+1):
    spaces=" " * (n-i)
    num=""
    for j in range(s,i+s):
        num+=str(j)+" "
    print(spaces+num)
    