L = ["5", "eat", "9.80", "Water", "python", "-678", "7685.26", "-2.5", "sing"]

# Write your code here
s=input()

for char in L:
    if s==char:
        print("True")
        break
else:
    print("False")