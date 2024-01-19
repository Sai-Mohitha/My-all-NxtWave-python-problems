string=input()
first_three_characters=string[:3]=="NXT"
remaining_characters=(int(string[3:]))%2==0 or (int(string[3:]))%7==0
if (first_three_characters)and(remaining_characters):
    print("Special String")
else:
    print("Not a Special String")