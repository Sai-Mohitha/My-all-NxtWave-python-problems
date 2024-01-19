a=input()
b=input()

result=""
for i in range(len(a)):
    if b.startswith(a[i:]):
        result=a[i:]
        break
if result=="":
    print("No overlapping")
print(result)    