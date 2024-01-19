m,n=list(map(int,input().split()))
new_list=[]
for i in range(m):
    num=list(map(int,input().split()))
    new_list.append(num)
    
num_list=[]    
for i in range(m):
    num=list(map(int,input().split()))
    num_list.append(num)

for  i in range(m):
    a=[]
    for j in range(n):
        a.append(new_list[i][j]+num_list[i][j])
    print(a)    
    
    
'''
Input:
3 3
1 2 3
10 20 30
5 10 15
2 4 6
11 22 33
7 14 21

Output:
[3, 6, 9]
[21, 42, 63]
[12, 24, 36]

'''    