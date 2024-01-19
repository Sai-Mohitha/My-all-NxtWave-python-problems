a=list(map(int,input().split()))
sum_dict={}
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        sum_dict[tuple(a[i:j])]=sum(a[i:j])
keys=list(sum_dict.keys())  
values=list(sum_dict.values())
max_sum_index=values.index(max(values))
print(*keys[max_sum_index])

'''
Question: Max Contiguous Subarray
Given a list of integers, write a program to identify the contiguous sub-list that has the largest sum and print the sub-list. Any non-empty slice of the list with step size 1 can be considered as a contiguous sub-list.

Approach
To solve this problem, we will follow these steps:

Read the input list of integers.
Iterate through the list and calculate the sum of all possible contiguous subarrays.
Find the subarray with the maximum sum and print it.
Step-by-Step Explanation
Step 1: Read the input and create an empty dictionary

First, we need to read the input list of integers. We can use the input() function to read the input and split() to separate the integers. Then, we can use map() and list() to convert the input into a list of integers.

After that, we will create an empty dictionary called sum_dict to store the sum of each contiguous subarray.

PYTHON
Step 2: Iterate through the list and calculate the sum of contiguous subarrays

Now, we will use two nested loops to iterate through the list and calculate the sum of all possible contiguous subarrays. For each subarray, we will store its sum in the sum_dict dictionary with the subarray as the key and the sum as the value.

PYTHON
Step 3: Find the subarray with the maximum sum and print it

Finally, we will find the subarray with the maximum sum and print it. To do this, we will convert the keys and values of the sum_dict dictionary into two separate lists. Then, we will find the index of the maximum sum in the values list and use it to get the corresponding subarray from the keys list. We will print the subarray using the print() function with the * operator to unpack the elements.



'''