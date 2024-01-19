'''
Question: Palindrome
In this coding question, you are given a string, and you need to check if the given string is a palindrome. A palindrome is a sequence of characters that can be read the same way whether you start from the beginning or the end. Remember that uppercase and lowercase characters are considered different.

'''

s=input()
if s==s[::-1]:
    print(True)
else:
    print(False)