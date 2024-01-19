s = input().split()
l=[]
if len(s)%2==1:
    cut = len(s)+1
    by = (cut//2) 
    for i in range(by):
        r = s[i]
        l.append(r)
else:
    by = (len(s)//2)
    for i in range(by):
        r = s[i]
        l.append(r)
print(l)        