def get_even_numbers_count(numbers):
    # complete this function
    count=0
    numbers=numbers.split()
    for i in (numbers):
        a=int(i)
        if a%2==0:
            count+=1 
            
    return count       

numbers = input()
result =get_even_numbers_count(numbers) # call the get_even_numbers_count function
print(result)