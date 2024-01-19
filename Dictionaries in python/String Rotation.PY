s1=input()
s2=input()


for i in s2:
    if len(s1)!=len(s2):
        result=("No match")
    elif s1[0]==i:
        result=(s2.index(i))
        break
    else:
        result=("No match")
print(result)        