from datetime import datetime
d_f="%b %d %Y %I:%M%p"
input_date=input()
d_t=datetime.strptime(input_date,d_f)
o_t="%d/%m/%Y %H:%M:%S"
f_d=datetime.strftime(d_t,o_t)
print(f_d)
'''
input:
Jul 01 2014 02:43PM
output:
01/07/2014 14:43:00
'''