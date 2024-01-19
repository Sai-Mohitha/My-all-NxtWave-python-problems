'''
Question: Kth Smallest Number
Write a program to print the Kth smallest number in the list.

Input:

The first line of input will contain comma-separated integers.
The second line of input will contain an integer (K).
Output:

The output should be a single line containing the Kth smallest number in the list.
'''
numbers = input()
k = int(input())

nums_list = numbers.split(",")

length_of_nums_list = len(nums_list)
for i in range(length_of_nums_list):
    nums_list[i] = int(nums_list[i])

nums_list = sorted(nums_list)
kth_smallest_number = nums_list[k-1]
print(kth_smallest_number)
