string=input().lower().split(" ")



dect_let={"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"10","k":"11",
            "l":"12","m":"13","n":"14","o":"15","p":"16","q":"17","r":"18","s":"19","t":"20","u":"21",
            "v":"22","w":"23","x":"24","y":"25","z":"26"," ":" "
    }
    
 
new_list=[]
for i in string:
    s=""  
    s=i[0]
    for j in dect_let.keys():
        if s==j:
            s_c=dect_let[j]
    r_c=i[1:]   
    p=""
    for k in r_c:
        for h in dect_let.keys():
            if k==h:
                p+="-"+dect_let[k]
    n_c=s_c+p 
    new_list.append(n_c)
r=" ".join(new_list)
print(r)
    
    