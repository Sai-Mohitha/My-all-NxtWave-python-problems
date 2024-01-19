n=int(input())
factor=0
for i in range(2,n):
    if(n%i==0):
        factor+=1 
if factor==0:
    print("Prime Number")
else:
    print("Not a Prime Number")
    
'''
Understanding Prime Numbers:
A prime number is a number greater than 1 that has only two factors: 1 and itself. For example, 2, 3, 5, and 7 are prime numbers.
'''    