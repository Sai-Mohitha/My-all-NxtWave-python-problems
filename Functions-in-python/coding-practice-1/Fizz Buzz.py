def fizz_buzz(number):
    # Complete this function
    if (number%3==0) and (number%5==0):
        result="FizzBuzz"
    elif (number%3==0):
        result="Fizz"
    elif (number%5==0):
        result="Buzz"
    else:
        result = number
    return result    

number = int(input())
# Call the fizz_buzz function
result = fizz_buzz(number)
print(result)