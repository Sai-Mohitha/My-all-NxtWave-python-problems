num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# Write your code here
n=input().split()
l=[]
for i in n:
    a=int(i)
    num_set.discard(a)
print(sorted(list(num_set)))
   