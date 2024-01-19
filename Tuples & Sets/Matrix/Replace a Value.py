def replace_old_value_with_new_value(matrix, old_value, new_value):
    # Complete this function
    update_matrix=[]
    for row in matrix:
        update_row=row
        for i in range(len(row)):
            if row[i]==old_value:
                update_row[i]=new_value
        update_matrix.append(update_row)
    return update_matrix    

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

values = input().split()
old_value, new_value = convert_string_to_int(values)

# Call the replace_old_value_with_new_value function
# Write your code here
update_matrix=replace_old_value_with_new_value(num_list,old_value,new_value)
for row in update_matrix:
    print(row)
