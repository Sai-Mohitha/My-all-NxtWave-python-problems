n=int(input())
l=[]
for num in range(n):
    commad=input().split()
    if commad[0]=="insert":
        index=int(commad[1])
        value=int(commad[2])
        l.insert(index,value)
    elif commad[0]=="append":
        value=int(commad[1])
        l.append(value)
    elif commad[0]=="pop":
        l.pop()
    elif commad[0]=="remove":
        value=int(commad[1])
        l.remove(value)
    elif commad[0]=="sort":
        l.sort()
    elif commad[0]=="print":  
        print(l)
    
'''
INPUT:
5
append 5
insert 0 2
append 1
sort
print

OUTPUT:
[1, 2, 5]

'''    