num_set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Write your code here
string=list(map(int,input().split()))
num_set_2=set(string)

if (num_set_1.issuperset(num_set_2)):
    print("Superset") 
elif (num_set_1.issubset(num_set_2)):
    print("Subset")
else:
    print("Disjoint Set")
    
    
'''
Question: Set Relation
In this problem, you are given a set of numbers. Your task is to write a program that checks the following relations with the given set:

Superset
Subset
Disjoint Set
You will receive a single line input containing space-separated integers. The output should be a single line containing either "Superset", "Subset", or "Disjoint Set".

For example, if the given input is "2 3 4", the output should be "Superset", as all the values in the given set are present in the original set.
'''    