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

# Write your code here
row_wise_max=[]
for row in num_list:
    row_wise_max.append(max(row))
maximum=max(row_wise_max)
row_index_containing_max=row_wise_max.index(maximum)
max_row=num_list[row_index_containing_max]
print(max_row)

colum_index_containing_max=max_row.index(maximum)
max_colum=[]
for row in num_list:
    max_colum.append(row[colum_index_containing_max])
print(max_colum)    

'''
Input:
3 3
1 2 3
10 20 30
5 10 15

Output:
[10, 20, 30]
[3, 30, 15]


'''



    
    
    
    