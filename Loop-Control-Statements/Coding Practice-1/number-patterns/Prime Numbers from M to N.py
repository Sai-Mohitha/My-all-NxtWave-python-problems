m=int(input())
n=int(input())
a=""
if not(m>1):
    m=2 
for i in range(m,n+1):
    factors=0 
    for j in range(2,i):
        if (i%j)==0:
            factors+=1 
    if factors==0:
        a+=str(i)+" "
if len(a)>=1:
    print(a)
else:
    print("No Prime Numbers Found")
     
    