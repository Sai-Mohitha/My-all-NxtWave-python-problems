rows = int(input())

# Upper half of diamond
for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        print(j, end=" ")
    print()

# Lower half of diamond
for i in range(rows-1, 0, -1):
    for j in range(rows-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        print(j, end=" ")
    print()