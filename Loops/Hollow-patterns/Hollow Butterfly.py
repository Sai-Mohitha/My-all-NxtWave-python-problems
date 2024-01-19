num=int(input())
print("* "+"  "*(num*2-2)+"*")
for i in range(2,num+1):
    value=(num*2)-(i*2)
    print("* "+("  "*(i-2))+"* "+("  "*value)+"* "+("  "*(i-2))+"*")
for i in range(num-1):
    value=num-i
    valu=num-i-2
    print("* "+("  "*(value-2))+"* "+("  "*(i*2))+"* "+("  "*valu)+"*")
print("* "+"  "*(num*2-2)+"*")