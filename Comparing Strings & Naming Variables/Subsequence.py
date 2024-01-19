w=input()
s=input()

s_index=0 
s_l=len(s) 

for char in w:
    if char==s[s_index]:
        s_index+=1 
        if s_index==s_l:
            break
if s_index==s_l:
    print("Yes")
else:
    print("No")