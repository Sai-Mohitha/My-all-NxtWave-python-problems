n=int(input())


sum=0
for i in range(1,n+1):
    num=int(input())
    sum+=num 
    average=(sum/i) 
   
    print(round(average,3))