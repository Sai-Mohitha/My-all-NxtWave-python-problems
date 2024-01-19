def cover_str_to_int(n):
    new_list=[]
    for i in n:
        new_list.append(int(i))
    if( len(set(new_list)))==1:
        print("True")
    else:
        print(sorted(list(set(new_list))))
    
n=input().split() 
cover_str_to_int(n)