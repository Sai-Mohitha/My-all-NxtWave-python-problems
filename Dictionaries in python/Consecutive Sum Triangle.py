def con_to_sum(num):
    new_list=[]
    for i in range(len(num)-1):
        c=num[i]+num[i+1]
        new_list.append(c)
    return new_list
def triangle(num):
    while len(num)>1:
        con=con_to_sum(num)
        print(con)
        num=con 
    return    
    
a=list(map(int,input().split(",")))
print(a)
triangle(a)