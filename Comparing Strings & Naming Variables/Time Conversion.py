t=input() #time 


a=(t[-1:]) #last character
b=(t[:-1]) #digits

m=int(b)/60  #minutes 
s=int(b)/3600 #seconds 

if (a=="M"):
    print(str(round(m,2))+"H")
else:
    print(str(round(s,2))+"H")
    