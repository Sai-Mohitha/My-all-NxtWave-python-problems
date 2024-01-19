n=int(input())
years=int(n/365)
rem_days=n-(years)*365
weeks=int(rem_days/7)
days=int(rem_days)-(weeks)*7

a=str(years)
b=str(weeks)
c=str(days)

result=(a+" "+"years"+" "+ b+" "+"weeks"+" "+c+" "+"days")
print(result)