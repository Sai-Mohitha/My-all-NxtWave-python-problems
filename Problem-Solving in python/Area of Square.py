m,n=map(int,input().split())
s=[]
for i in range(m):
    num=list(map(str,input().split()))
    s.append(num)
    
    
b=[[0 for i in range(n+1)]for j in range(m+1)] 

area=0
for i in range(1,m+1):
    for j in range(1,n+1):
        if(s[i-1][j-1])=="X":
            b[i][j]=min(b[i-1][j-1],b[i-1][j],b[i][j-1])+1 
            area=max(area,b[i][j])
print(area*area)            
            
'''
Approach
To solve this problem, we will follow these steps:

1)Read the matrix from the input.
2)Check if a sub-matrix contains 'O'.
3)Get the maximum sub-matrix area for each 'X' in the matrix.
4)Get the maximum area of square containing only 'X's.
5)Implement the main function to execute the above steps.

input:
4 5
X O X O O
X O X X X
X X O X X
X O O X O

output:
4
'''            
        
       
    
