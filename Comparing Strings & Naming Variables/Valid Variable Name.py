s=input()

for i in s:
    if i.isdigit() or i.isalpha():
        result=(True)
    else:
        result=(False)
        break
print(result)    
    