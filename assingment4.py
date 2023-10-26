import math
operation=input("please enter operation(+,-,*,/,sin,cos,tan,cot,factorial,sqrt):")
if operation=="+"or operation=="-"or operation=="*"or operation=="/":
    a=float(input("enter a:"))       
    b=float(input("enter b:"))
    if  operation=="+":
        c=a+b
        print(c)
    if  operation=="-":
        c=a-b
        print(c)
    if  operation=="*":
        c=a*b
        print(c)
    if  operation=="/":
        if b==0:
            print("b can not equal to 0")
        else:    
            c=a/b
            print(c)
if operation=="sin" or operation=="cos" or operation=="tan" or operation=="cot" or operation=="sqrt" or operation=="factorial":
    a=float(input("please enter the number:")) 
    pi=math.pi   
    if  operation=="cos":
        a=(a*pi)/180
        c= math.cos(a)
        print(round(c,2))
    if operation=="sin":
        a=(a*pi)/180
        c= math.sin(a)
        print(round(c,2))
    if operation=="tan":
        a=(a*pi)/180
        if round(math.cos(a),2)==0:
            print("Eroor")
        else:
            c= math.tan(a)
            print(round(c,2)) 
    if operation=="cot":
        a=(a*pi)/180
        if round(math.sin(a),2)==0:
            print("Eroor")
        else:
            c= 1/(math.tan(a))
            print(round(c,2)) 
    if operation=="factorial":
        if a<0:
            print("Eroor")
        else:
            c= math.factorial(int(a))
            print(c)  
    if operation=="sqrt":
        if a<0:
            print("Eroor")
        else:
            c= math.sqrt(a)
            print(c)     
else:              
    print("wrong operation, the calculator program only defines for +,-,*,/,sin,cos,tan,cot,factorial,sqrt")
