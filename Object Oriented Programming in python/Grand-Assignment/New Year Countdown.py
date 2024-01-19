from datetime import datetime,timedelta

d=input()
date_time="%b %d %Y %I:%M %p"
d1=datetime.strptime(d,date_time)
d2=datetime(2021,1,1)
dt=d2-d1
h=dt.days*24+dt.seconds//3600
m=(dt.seconds//60)%60
print("{} hours {} minutes".format(h,m))
