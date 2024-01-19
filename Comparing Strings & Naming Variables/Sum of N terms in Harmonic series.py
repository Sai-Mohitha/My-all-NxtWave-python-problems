n=int(input())

sum=0 

for i in range(1,n+1):
    harmonic_series=1/i 
    sum+= harmonic_series
print(round(sum,2))