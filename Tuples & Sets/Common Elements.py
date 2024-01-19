def convert_string_to_int(a,b):
    new_list=[]
    for i in a:
        num=int(i)
        new_list.append(num)
    b_new_list=[]
    for i in b:
        num=int(i)
        b_new_list.append(num)

    a_b=set(new_list)&set(b_new_list)
    print(sorted(list(a_b)))
    
a=input().split(",")    
b=input().split(",")    

convert_string_to_int(a,b)