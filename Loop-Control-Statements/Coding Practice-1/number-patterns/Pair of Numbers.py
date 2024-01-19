n = int(input())

count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i < j) and (i + j)==n:
            count += 1
print(count)            