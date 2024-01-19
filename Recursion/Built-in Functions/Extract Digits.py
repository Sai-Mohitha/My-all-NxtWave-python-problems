s=input()
l=[]

for char in s:
    if char.isdigit():
        l+=[int(char)]
print(sum(l))  
print(min(l))
print(max(l))

'''
Tutorial: Extract Digits
Step 1: Define a function to get the digits
First, we'll create a function called get_digits that takes a string as an input and returns a list of digits found in the string.

Explanation:
Create an empty list called digits_list to store the digits.
Loop through each character in the input string using a for loop.
Check if the character is a digit using the isdigit() method. If it is, convert the character to an integer and add it to the digits_list.
PYTHON
Step 2: Get the input string
Now, we'll ask the user to enter a string and store it in a variable called str_1.

PYTHON
Step 3: Extract the digits
We'll use the get_digits function that we created in Step 1 to extract the digits from the input string str_1.

PYTHON
Step 4: Calculate the sum, minimum, and maximum
Now that we have the digits in a list, we can calculate the sum, minimum, and maximum of these digits using Python's built-in functions sum(), min(), and max().

PYTHON
Step 5: Print the results
Finally, we'll print the sum, minimum, and maximum of the digits, each on a new line.

PYTHON
Now that we have all the steps, put them together and solve the question.
'''