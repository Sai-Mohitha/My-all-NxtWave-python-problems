n=int(input())
k=int(input())

last_num=(n-1)
for i in range(k):
    for j in range(i+1):
        last_num+=1 
        
for i in range(k):
    string=""
    
    for i in range(i+1):
        string+=str(last_num)+" "
        last_num=last_num-1 
    print(string)
    