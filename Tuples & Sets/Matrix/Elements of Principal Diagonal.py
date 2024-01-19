m,n=list(map(int,input().split()))

new_list=[]
for i in range(m):
    num=list(map(int,input().split()))
    new_list.append(num)
    
num_list=[]   
z=n-1
for i in range(n):
    a=[]
    for j in range(m):
        a.append(new_list[i][z-i])
    num_list.append(a[0])   
print(num_list)