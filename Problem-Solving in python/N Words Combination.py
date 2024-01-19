from itertools import combinations

string=input().split()
string.sort()
n=int(input())


lenght=list(range(len(string)))
stored=set()
com=combinations(lenght,n)

for i in com:
    s=""
    for j in range(len(i)):
        s+=string[i[j]]+" "
    stored.add(s)    
result=list(stored)  
result.sort()

for i in result:
    print(i)

'''
input:
apple is a fruit
3

output:
a apple fruit 
a apple is 
a fruit is 
apple fruit is 

'''