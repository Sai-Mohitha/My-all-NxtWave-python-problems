from datetime import datetime
d="%d %b %Y"
s=input()
date_time_obj=datetime.strptime(s,d)
print(date_time_obj)


'''
SAMPLE INPUT:
2 Jul 2000

SAMPLE OUTPUT:
2 Jul 2000

Let's break down the solution into simple steps and explain each one:

Step 1: Import the required module
First, we need the datetime module to work with dates and times in Python.

PYTHON
Step 2: Set the date format
We have a date format to work with: "8 Feb 2021". We'll create a variable for this format.

PYTHON
Step 3: Read the input date
Now, we'll get the input date from the user.

PYTHON
Step 4: Convert the input date to a datetime object
We'll use the strptime function to convert the input date string into a datetime object. This function takes two arguments - the date string and the format of the date string.

PYTHON
Step 5: Print the datetime object
Finally, we'll print the datetime object, which will display the date and time in the default format (YYYY-MM-DD HH:MM:SS). Since the time is not given, it will show as 00:00:00.

PYTHON

Submit Feedback
Completed


'''