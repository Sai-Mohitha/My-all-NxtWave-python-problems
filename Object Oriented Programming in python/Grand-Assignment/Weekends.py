import datetime 
s1=input()
s2=input()


start_date=datetime.datetime.strptime(s1,"%d %b %Y")
end_date=datetime.datetime.strptime(s2,"%d %b %Y")
day=datetime.timedelta(days=1)
c_saturdays=0
c_sundays=0 
while start_date<=end_date:
    if start_date.isoweekday()==6:
        c_saturdays+=1 
    elif start_date.isoweekday()==7: 
        c_sundays+=1
    start_date+=day
print("Saturday:",c_saturdays) 
print("Sunday:",c_sundays)


'''
input:
25 Jan 2021
14 Feb 2021

output:
Saturday: 3
Sunday: 3
'''