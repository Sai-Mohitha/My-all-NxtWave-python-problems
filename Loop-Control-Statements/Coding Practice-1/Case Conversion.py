s=input()
c=0 
r=""
for i in s:
    if i.isupper():
        if c==0:
            r=r+i.lower()
            c=c+1 
        else:
            r=r+"-"+i.lower()
    else:
        r=r+i 
print(r)        