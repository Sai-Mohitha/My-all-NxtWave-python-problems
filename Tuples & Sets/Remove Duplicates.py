string=input().split()

l=[]
for i in string:
    a=int(i)
    l.append(a)
    
num_set=set(l)
num_list=list(num_set)
num_list.sort()
print(num_list)