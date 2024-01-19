n=int(input())
a=n%100 
b=a%50 
c=b%10 
d=c%1 

print("100:"+str(n//100))
print("50:"+str(a//50))
print("10:"+str(b//10))
print("1:"+str(c//1))