string = input()
p=[]
for each in string:
    if each.isupper():
        break
    p.append(each)
lenght = len(p)
result = string[lenght]
print(ord(result))