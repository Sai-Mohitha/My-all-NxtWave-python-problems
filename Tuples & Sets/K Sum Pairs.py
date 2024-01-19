string=set(map(int,input().split(",")))
n=int(input())
list_string=sorted(list(string)) 
lenght_of_string=len(list_string)
count=0 
for i in list_string:
    for j in range(count+1,lenght_of_string):
        j=list_string[j] 
        j=int(j)
        if (i+j)==n:
            pair=(i,j)
            print(tuple(pair))
            count+=1