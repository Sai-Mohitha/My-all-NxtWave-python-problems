set_a = {"pencil"}

word = input().split()
set_a.update(word)

list_a = list(set_a)
list_a.sort()
print(list_a)
