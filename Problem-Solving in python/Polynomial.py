n=int(input())
store1=[]
for i in range(n):
    m=list(map(int,input().split()))
    store1.append(m)
store1=sorted(store1,reverse=True)    
store=""
a=True

for i in store1:
    pi=i[0]
    ci=i[1]
    if a:
        store+=str(ci)+"x^"+str(pi)
        a=False 
    else:
        if ci==1 and pi>0:
            store+=" + "+"x^"+str(pi)
        elif ci==-1 and pi>0:
            store+=" - "+"x^"+str(pi)  
        elif ci>0 and pi==1:
            store+=" + "+str(ci)+"x"    
        elif ci<0 and pi==1:
            store+=" - "+str(abs(ci))+"x"  
        elif ci>0 and pi>0:
            store+=" + "+str(ci)+"x^"+str(pi)
        elif ci<0 and pi>0:
            store+=" - "+str(abs(ci))+"x^"+str(pi)  
        elif ci==0 and pi==0:
            continue
        elif ci>0 and pi==0:
            store+=" + "+str(ci)
        elif ci<0 and pi==0:
            store+=" - "+str(abs(ci))
print(store)        
            
'''
Tutorial: Polynomial
What is a Polynomial?
A polynomial is a mathematical expression made up of variables, coefficients, and exponents, combined using addition, subtraction, and multiplication. A polynomial can have any number of terms, and each term has a coefficient and a power. A polynomial can be represented as:

Cnx^n + Cn-1x^n-1 + ... + C2x^2 + C1x + C_0

where Cn, Cn-1, ..., C_0 are coefficients, x is the variable, and n is the degree of the polynomial.

Now that you know what a polynomial is, let's learn how to write a program that prints a polynomial in a specific format. We will explain the solution step by step so that you can easily understand and follow along.

Step 1: Read the input polynomial
First, we need to read the input polynomial as a dictionary with the power as the key and the coefficient as the value.

PYTHON
Step 2: Create a term for each coefficient and power
We need to create a polynomial term for each given coefficient and power, excluding the sign. The term should follow the format mentioned in the question.

 
PYTHON
Step 3: Generate the polynomial expression string
Now, we need to generate the polynomial expression string by iterating through the dictionary and combining the terms created in Step 2.

 
PYTHON
Step 4: Main function
Finally, we will create a main function that calls the functions we defined in the previous steps to read the polynomial, generate the expression string, and print the output.

PYTHON
That's it! You have now learned what a polynomial is and how to write a program that prints a polynomial in a specific format. Practice this program and try to understand each step. Happy coding!
'''            
            
            
            
            
            
            
            