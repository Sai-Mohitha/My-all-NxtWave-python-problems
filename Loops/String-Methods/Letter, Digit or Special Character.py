c=input()


if c.isdigit():
    print("Digit")
elif c!=c.lower():
    print("Uppercase Letter") 
elif c!=c.upper():
    print("Lower Letter")
else:
    print("Special Character")