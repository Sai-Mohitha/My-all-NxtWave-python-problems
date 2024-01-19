def str_to_int(num_list):
    new_list=[]
    for i in num_list:
        num=int(i)
        new_list.append(num)
    return new_list 
n=int(input())  
now_list=[]
for i in range(n):
    values_list=input().split()
    values_list=str_to_int(values_list)
    values_set=set(values_list)
    is_eqaul=len(values_list)==len(values_set)
    if is_eqaul:
        now_list.append(values_list)
print(now_list)    