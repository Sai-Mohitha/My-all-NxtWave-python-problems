n=int(input())
a=int(2)
b=int(3)
l_2=[]
l_3=[]
s_2=[]
for i in range(1,n+1):
    m_2=a*i
    s_2+=[m_2]
    sm_2=set(s_2)
    if m_2%3==0:
        continue 
    l_2+=[m_2]
print(l_2)     

for i in range(1,n+1):
    m_3=b*i 
    l_3+=[m_3]
    sm_3=set(l_3)
    
sm_2=sm_2 
sm_3=sm_3 
print(list(sm_2^sm_3))





    

   
    
    
    
    
    
    