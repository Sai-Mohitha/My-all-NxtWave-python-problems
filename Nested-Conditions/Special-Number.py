n=input()
sum_of= int(n[0])+int(n[1])
equal_to=(sum_of)==7
one_of=(int(n[0]))==7 or (int(n[1]))==7
n=int(n)
divisible_by_7=(n%7)==0
if (equal_to)or(one_of)or(divisible_by_7):
    
    print("Special Number")
else:
    print("Normal Number")
    
    
'''
In this question, we need to find the following Three cases and print the string accordingly.

	1. The sum of digits is 7

	2. One of the digits is 7

	3. The number is a multiple of 7

Let us assume the number as 67

And perform each of the checks mentioned in the question and print accordingly
'''    