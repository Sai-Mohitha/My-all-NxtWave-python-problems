a=input()
b=input()

c=a[:3]=="DIS" or b[:3]=="DIS"

if c:
    print("Discount")
else:
    print("No Discount")