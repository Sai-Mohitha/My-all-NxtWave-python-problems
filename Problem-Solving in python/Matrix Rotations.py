def read_matrix(n):
    matrix=[]
    for i in range(n):
        row=list(map(int,input().split()))
        matrix.append(row)
    return matrix
def single_roration_clockwise(matrix):
    n=len(matrix[0])
    temp_matrix=[]
    for i in range(n):
        column=[]
        for row in matrix:
            column.append(row[i])
        temp_matrix.append(column[::-1])  
    return temp_matrix
def rotare_matrix(matrix,degrees):
    n=len(matrix[0])
    rotations=(degrees//90)%4
    for r in range(rotations):
        matrix=single_roration_clockwise(matrix)
    return matrix
def main():
    n=int(input())
    matrix=read_matrix(n)
    original_matrix=matrix
    total_rotations=0 
    while True:
        line=input().split()
        if line[0]=="-1":
            break
        elif line[0]=="R":
            rotations=int(line[1])
            total_rotations+=rotations
            matrix=rotare_matrix(matrix,rotations)
        elif line[0]=="U" :
            ri,ci,value=int(line[1]),int(line[2]),int(line[3])
            original_matrix[ri][ci]=int(value)
            matrix=rotare_matrix(original_matrix,total_rotations)
        elif line[0]=="Q" :
            ri,ci=int(line[1]),int(line[2])
            print(matrix[ri][ci])
main()            
        
            
    
    
    
    
'''
input:
2
1 2
3 4
R 90
Q 0 0
Q 0 1
R 90
Q 0 0
U 0 0 6
Q 1 1
-1

output:
3
1
4
6

'''    