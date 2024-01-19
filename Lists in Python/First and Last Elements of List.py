n=int(input())

s=[]
for i in range(n):
    a=int(input())
    s+=[a] 
List=(s)
first_part=List[:2]
second_part=List[-2:]
print(first_part+second_part)