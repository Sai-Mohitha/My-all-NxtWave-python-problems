L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]

#Write your code here
l_1=int(input())
l_2=int(input())

L[l_1],L[l_2]=L[l_2],L[l_1]
print(L)
