def check_is_prime(m, n):
    
    # complete this function
    s=[]
    if not(m>1):
        m=2
    for i in range(m,n+1):
        count=0 
        for j in range(2,i):
            if i%j==0:
                count+=1 
        if count==0:
            s+=[str(i)] 
    space=" ".join(s)        
    return space
    
m = int(input())
n = int(input())

prime_numbers = check_is_prime(m, n)   # Call the check_is_prime function

print(prime_numbers)