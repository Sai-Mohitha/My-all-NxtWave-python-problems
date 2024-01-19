students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
n=int(input())
for i in range(n):
    key,value=input().split()
    students_dict[key]=value 
print(students_dict)