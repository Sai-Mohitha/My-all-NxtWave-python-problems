m,n=list(map(int,input().split()))

new_list=[]
for i in range(m):
    num=list(map(int,input().split()))
    new_list.append(num)
end_index=m+n-1

for i in range(end_index):
    for j in range(i+1):
        if j<m and i-j<n:
            print(new_list[j][i-j],end=" ")
            
    print()        