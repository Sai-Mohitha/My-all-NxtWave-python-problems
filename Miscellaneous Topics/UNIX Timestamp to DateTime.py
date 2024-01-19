import datetime

zero=datetime.datetime(1970,1,1)
u=int(input())
seconds=datetime.timedelta(seconds=u)
result_time=zero+seconds
dt_farmate="%Y-%m-%d %H:%M:%S"

print(result_time.strftime(dt_farmate))
