def sum_of_cubes_m_to_n(m, n):
    # Complete this function
    sum=0 
    for i in range(m,n+1):
        cubes=(i**3)
        sum+=cubes 
    print(sum)
        
    

m = int(input())
n = int(input())
# Call the sum_of_cubes_m_to_n function
sum_of_cubes_m_to_n(m,n)
