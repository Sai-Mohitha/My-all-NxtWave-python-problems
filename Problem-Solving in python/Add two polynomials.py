def read_polynomial():
    n=int(input())
    polynomial_dict={}
    for i in range(n):
        power,coefficent=map(int,input().split())
        polynomial_dict[power]=coefficent
    return polynomial_dict    
def get_term(coefficent,power):
    coefficent=abs(coefficent)
    if coefficent==1 and power!=0:
        coefficent=''
    if power > 1:
        term = "{}x^{}".format(coefficent,power)
    elif power == 1:
        term = "{}x".format(coefficent)
    elif power == 0:
        term ="{}".format(coefficent)
    return term 
def get_polynomial_expression_string(polynomial):
    expression=""
    degree=max(polynomial.keys())
    for power in sorted(polynomial.keys(),reverse=True):
        coefficent=polynomial[power]
        term=get_term(coefficent,power)
        if power == degree:
            if coefficent>0:
                expression=term 
            elif coefficent < 0:
                expression="-{}".format(term)
        else:
            if coefficent>0:
                expression="{} + {}".format(expression,term)
            elif coefficent<0:
                expression ="{} - {}".format(expression,term)
    if expression =="" :
        expression=0 
    return expression 
    
def get_coefficent(polynomial,power) :
    try:
        return polynomial[power]
    except KeyError:
        return 0 
def add (p1,p2):
    result=dict()
    for power in (set(p1.keys())|set(p2.keys())):
        result[power]=get_coefficent(p1,power)+get_coefficent(p2,power)
    return result 
    
def main():
    p1=read_polynomial()
    p2=read_polynomial()
    result=add(p1,p2)
    print(get_polynomial_expression_string(result))
    
main()    
    
    
'''
input:

4
0 5
1 0
2 10
3 6
3
0 1
1 2
2 4

output:
6x^3 + 14x^2 + 2x + 6
'''    
    
        
    
        
    
    
                
    
    
    
    
    