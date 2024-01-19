s=input().split()
vowels="a","e","i","o","u","A","E","I","O","U"

for i in s:
    p=[]
    p.append(i)
    for j in p:
        if j in vowels:
            break
        print(j)
    