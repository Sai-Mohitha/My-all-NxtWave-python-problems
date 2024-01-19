unites=int(input())

if unites<50:
    bill=2*unites
elif unites<150:
    bill=(2*50)+(3*(unites-50))
elif unites<250:
    bill=(2*50)+(3*100)+(5*(unites-150))
elif unites>=250:
    bill=(2*50)+(3*100)+(5*100)+(8*(unites-250))
print(bill*0.2+bill)    