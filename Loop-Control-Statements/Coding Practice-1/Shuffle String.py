'''
Question:

For a given string and N integers, where N is the length of the string, we've to shuffle the characters of the string as per the order of the integers given and print the shuffled string.


'''

s=input()
len_s=len(s)
shuffled_s=""
for i in range(len_s):
    index=int(input())
    shuffled_s+=s[index]
print(shuffled_s)    