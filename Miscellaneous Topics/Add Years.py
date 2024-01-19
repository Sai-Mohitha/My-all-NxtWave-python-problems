from datetime import datetime,timedelta
input_of=input()
n=int(input())
f_of="%b %d %Y" 
date_of=datetime.strptime(input_of,f_of)
d_2=date_of+timedelta(365*n)
print(d_2)

'''
input:
Jul 11 2014
5

output:
2019-07-10 00:00:00
'''