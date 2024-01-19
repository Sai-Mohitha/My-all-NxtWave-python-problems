m = int(input())
n = int(input())
sum=0
if not(m>1):
    m=2
for i in range(m,n+1):
    factors=0
    for j in range(2,i):
        if (i % j)==0:
            factors+=1 
    if factors == 0:
        sum+=i
print(sum)