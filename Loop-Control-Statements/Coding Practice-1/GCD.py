m = int(input())
n = int(input())
if m > n:
  smallest_number = m
else:
  smallest_number = n
gcd = smallest_number

for i in range(1, smallest_number+1):
  if ((m % i) == 0) and ((n % i) == 0):
        gcd=i 
print(gcd)        