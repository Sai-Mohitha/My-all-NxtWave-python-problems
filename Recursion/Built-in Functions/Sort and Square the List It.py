list_a = input().split(",")
list_x = []

for num in list_a:
    list_x += [int(num)**2]
list_x=sorted(list_x)
print(list_x)