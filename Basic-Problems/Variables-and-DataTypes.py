Number = "Hello World!" #Here "Number" is a variable 
#And the equals to = sign is called as Assignment Operator as it is used to assign values to variables.
print(Number)

'''
data types:
In programming languages, every value or data has an associated type to it known as data type.
Some commonly used data types
1)String
2)Integer
3)Float
4)Boolean
This data type determines how the value or data can be used in the program. For example, mathematical operations can be done on Integer and Float types of data.
'''

#string:A String is a stream of characters enclosed within quotes.
#For example:

string = str("Hello Every One.")
print(type(string))

'''Integer:

All whole numbers (positive, negative and zero) without any fractional part come under Integers.
Examples:
...-3, -2, -1, 0, 1, 2, 3,...
'''
Integer = int(123) #here int() indicates integer datatype..
print(type(Integer)) #type() checks the datatypes.

'''
Float:
Any number with a decimal point
ex:
24.3, 345.210, -321.86...
'''
float = float(33.2)
print(type(float))

'''
Boolean:
In a general sense, anything that can take one of two possible values is considered a Boolean. Examples include the data that can take values like 

True or False
Yes or No
0 or 1
On or Off, etc.

As per the Python Syntax, True and False are considered as Boolean values.
Notice that both start with a capital letter.
'''
Boolean = bool(5>6)
print(type(Boolean))
print(Boolean)
