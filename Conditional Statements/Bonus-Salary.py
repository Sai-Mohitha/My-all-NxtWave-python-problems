salary=int(input())
year_of_service=int(input())
bonus=0.05*(salary)

if (year_of_service>5):
    print(bonus)
else:
    print("No Bonus")