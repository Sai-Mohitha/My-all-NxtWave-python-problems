s1=input()
s2=input() 

s=""

for i in range(len(s1)):
    if i%2==0:
        s+=s1[(i)]
    else:
        s+=s2[(i)]
print(s)       