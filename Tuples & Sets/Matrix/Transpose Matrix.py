def get_transpose_of_matrix(matrix, m, n):
    # Complete this function
    matrix_row=[]
    for i in range(n):
        num_list=[]
        for j in range(m):
            num_list.append(matrix[j][i])
        matrix_row.append(num_list)
    return matrix_row    
    

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

# Call the get_transpose_of_matrix function
result=get_transpose_of_matrix(num_list,m,n)
for i in result:
    print(i)
    
    
'''
Input:
3 3
1 2 3
10 20 30
5 10 15

Output:
[1, 10, 5]
[2, 20, 10]
[3, 30, 15]


'''    