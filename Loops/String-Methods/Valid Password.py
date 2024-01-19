#Question: Valid Password
'''
Write a program to check whether the given password is valid or not. Consider the password to be valid if it contains at least one uppercase letter, one lowercase letter, and one digit.

Input: The input will be a single line containing a string.

Output: The output should be a single line containing either "Valid Password" or "Invalid Password".

Example: If the given password is "Qwerty00", the output should be "Valid Password" as it contains an uppercase letter, a lowercase letter, and a digit. Whereas, if the given password is "Dashboard", the output should be "Invalid Password" as it does not contain a digit.
'''

password = input()

contains_digit = False
for character in password:
    is_digit = character.isdigit()
    if is_digit:
        contains_digit = True

is_all_lower = password.lower() == password
is_all_upper = password.upper() == password
contains_lower_and_upper = (not is_all_lower) and (not is_all_upper)

is_valid_password = contains_digit and contains_lower_and_upper

if is_valid_password:
    print("Valid Password")
else:
    print("Invalid Password")