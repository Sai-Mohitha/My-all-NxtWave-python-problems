n=input()

digits=(n[0]!="5") or (n[1]!="5") or (n[2]!="5")

n=int(n)
between=300<n<700
if (digits)and(between):
    print("Valid Number")
else:
    print("Not a Valid Number")