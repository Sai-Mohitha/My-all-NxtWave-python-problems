s=input().lower()

a="" 
for i in s:
    if i.isalpha():
        a+=chr(97+122-ord(i))
    else:
        a+=i 
print(a)        
'''
input:
python

output:
kbgslm
'''            