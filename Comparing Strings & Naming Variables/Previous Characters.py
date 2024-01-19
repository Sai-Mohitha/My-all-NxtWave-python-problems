s=input()

for i in s:
    if i == " ":
        continue 
    else:
        coverting = ord(i)-1 
        print(chr(coverting))
        