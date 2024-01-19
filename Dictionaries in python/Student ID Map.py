def convert_to_key_value_pair(key_lists,value_lists):
    dict_a={}
    number_of_keys=len(key_lists)
    for items in range(number_of_keys):
        key=key_lists[items]
        value=value_lists[items]
        dict_a[key]=value 
    return dict_a
    



student_names=input().split(",")
students_ids=input().split(",")
student_details=convert_to_key_value_pair(student_names,students_ids)
student_details_items=student_details.items()
student_details=sorted(student_details_items)
for i in student_details:
    print(*i)

'''
Input:
Anand,Ramesh,Kiran
ID102,ID101,ID100

Output:
Anand ID102
Kiran ID100
Ramesh ID101

'''