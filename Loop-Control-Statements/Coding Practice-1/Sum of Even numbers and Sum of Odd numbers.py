#Sum of Even numbers
n=int(input())
r=0
for i in range(1,n+1):
    if i%2==1:
        r+=i
    print(r)
    
#Sum of Odd Numbers
n=int(input())
sum=0 

for i in range(1,n+1):
    if i%2!=0:
        sum+=i 
print(sum)    