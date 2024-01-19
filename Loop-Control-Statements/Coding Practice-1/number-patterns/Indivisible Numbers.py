n=int(input())

count=0 

for i in range(1,n+1):
    is_divisible="True"
    for j in range(2,11):
        if (i%j==0):
            is_divisible="False"
            break
    if is_divisible == "True":
        count = count + 1
print(count)    