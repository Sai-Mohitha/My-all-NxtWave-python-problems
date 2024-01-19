new_list=[]
list_a=[]
for i in range(3):
    n=input().split()
    new_list.append(n)
    
for item in new_list:
    if item.count("O")==3:
        list_a.append("Abhinav Wins")
        break
    elif item.count("X")==3:
        list_a.append("Anjali Wins")
        break
    else:
        list_a.append("Tie")
        
vertical=[]  
for i in range(len(new_list)):
    ver=[]
    for j in range(len(new_list)):
        ver.append(new_list[j][i])
    vertical.append(ver)  
    
for item in vertical:
    if item.count("O")==3:
        list_a.append("Abhinav Wins")
        break
    elif item.count("X")==3:
        list_a.append("Anjali Wins")
        break
    else:
        list_a.append("Tie")
        
diagonals=[] 
anti_diagonals=[]

for i in range(len(new_list)):
    for j in range(len(new_list)):
        if i==j:
            diagonals.append(new_list[i][j])
            
        if j+i==2:
            anti_diagonals.append(new_list[i][j])
if diagonals.count("O")==3 or anti_diagonals.count("O")==3:
    list_a.append("Abhinav Wins")
elif diagonals.count("X")==3 or anti_diagonals.count("X")==3:
    list_a.append("Anjali Wins")
if "Anjali Wins" in list_a:
    print("Anjali Wins")
elif "Abhinav Wins" in list_a:
    print("Abhinav Wins")
else:
    print("Tie")

            
            
            
            
            
            

        