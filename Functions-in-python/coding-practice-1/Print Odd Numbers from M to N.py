def get_odd_numbers_in_range(start_number, end_number):
    
    # complete this function
 
    odd_numbers_list = []

    for each_number in range(start_number, end_number + 1):
        if each_number % 2 == 1:
            odd_numbers_list += [str(each_number)]
    
    space_separated_odd_numbers = " ".join(odd_numbers_list)
    return space_separated_odd_numbers

start_number = int(input())
end_number = int(input())

odd_numbers = get_odd_numbers_in_range(start_number, end_number)# Call the odd_numbers_in_range function
print(odd_numbers)