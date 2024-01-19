from datetime import datetime,timedelta
d1=input()
d2=input()
start_d=datetime.strptime(d1,"%b %d %Y")
end_d=datetime.strptime(d2,"%b %d %Y")

number_of_days=(end_d-start_d).days 

for i in range(number_of_days+1):
    print(start_d+timedelta(i))