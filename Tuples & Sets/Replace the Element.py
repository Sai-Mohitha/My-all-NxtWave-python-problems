num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
# Write your code here
n=int(input())
l=[]
for num in num_list:
    t=num[:-1]+(n,)
    l.append(t)
print(l)
    