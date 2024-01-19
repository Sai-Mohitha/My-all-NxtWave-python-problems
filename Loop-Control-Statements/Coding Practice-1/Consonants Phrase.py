sentence = input()
vowels = "a", "e", "i", "o", "u"
result = ""
for char in sentence:
    if char.lower() not in vowels: 
        result = result+char
print(result)

#Method-2:
w=input()

s=""

for i in w:
    x=i.lower() 
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
        s+=""
    else:
        s+=i 
print(s)    