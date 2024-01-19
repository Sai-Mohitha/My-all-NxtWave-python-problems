def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)
    
new_list=[]
for i in num_list:
    for j in i:
        new_list.append(j)
    
print(max(new_list))  
print(min(new_list))
print(sum(new_list))
    
    
    
    
'''
INPUT:
3 3
1 2 3
10 20 30
5 10 15

OUTPUT:
30
1
96
'''