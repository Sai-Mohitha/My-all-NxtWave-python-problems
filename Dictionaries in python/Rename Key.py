fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

# Write your code here
keys=input()
new_key=input()
fruit_items=list(fruits.items())
fruit_items_copy=fruit_items.copy()
lenght=len(fruit_items)

for i in range(lenght):
    if fruit_items[i][0]==keys:
        update_tuple=(new_key,fruit_items[i][1])
        fruit_items_copy[i]=update_tuple
print(fruit_items_copy)    