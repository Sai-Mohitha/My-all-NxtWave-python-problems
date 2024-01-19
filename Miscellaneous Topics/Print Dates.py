from datetime import datetime,timedelta
input_of=input()
date_string="%d %b %Y"
today=datetime.strptime(input_of,date_string)
yesterday=today-timedelta(days=1)
next_day=today+timedelta(days=1)
print(yesterday)
print(today)
print(next_day)