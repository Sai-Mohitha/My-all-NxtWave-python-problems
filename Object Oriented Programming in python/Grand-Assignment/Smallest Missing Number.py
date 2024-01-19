input_of=list(map(int,input().split()))
input_of.sort()

for i in range(1,10):
    if i not in input_of:
        print(i)
        break
    