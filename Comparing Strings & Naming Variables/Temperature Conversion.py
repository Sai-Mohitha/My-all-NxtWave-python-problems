t=input() 
f_t=float(t[:-1])
c_t=t[-1]

if c_t=="C":
    
    print(str(f_t)+"C")
    print(str(round((9*f_t)/5+32,2))+"F")
    print(str(round(f_t+273,2))+"K")
    
elif c_t=="F" :
    print(str(round((f_t-32)*5/9,2))+"C")
    print(str(f_t)+"F")
    print(str(round((f_t-32)*5/9+273,2))+"K")
    
elif c_t=="K":
    print(str(round(f_t-273,2))+"C")
    print(str(round((f_t-273) * 9/5+32,2))+"F")
    print(str(f_t)+"K")
    
    

    