w=input()
s=""

for i in w:
    x=i.lower()
    
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        s=s+""
    else:
        s=s+i 
print(s)        