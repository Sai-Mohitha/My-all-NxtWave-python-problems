months=int(input())

winter_season=(months==1) or (months==11) or(months==12)
Spring_season=(months==2) or (months==3)
Summer_season=(months==4) or (months==5) or (months==6)
rainy_season=(months==7) or (months==8)
autumn_season=(months==9) or (months==10)

if (winter_season):
    print("Winter")
elif(Spring_season):
    print("Spring")
elif(Summer_season):
    print("Summer")
elif(rainy_season):
    print("Rainy")
elif(autumn_season):
    print("Autumn")