n=int(input())
k=int(input())
sum=0 

for i in range(1,n+1):
   power=(i**k)
   sum+=power
print(sum)
