nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
# Write your code here
n=int(input())
occuresnces=nums_list.count(n)
for i in range(occuresnces):
    nums_list.remove(n)
print(nums_list)    
