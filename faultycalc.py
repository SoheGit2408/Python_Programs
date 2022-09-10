choice='y'
while(choice!='q'):
    a=float(input("Enter the first number \n"))
    b=float(input("Enter the second number \n"))
    print("choose any one of the following operation to be performed on above. two. numbers.")
    print("+","-","*","/","%","**",)
    c=input()
    if c=='+':
        if a==56 and b==9:     
            print("addition=",77)
        elif a==9 and b==56:        
             print("addition=",77)
        else :
             print("addition =", a+b)      
    elif c=='*':
         if a == 45 and b == 3:
             print("multiplication=", 555)
         elif a == 3 and b == 45:
             print("multiplication=", 555)
         else :
             print("multiplication=", a * b)
    elif c=='/':
         if a==56 and b==6:
             print("division =",4)
         else:
             print("division=", a / b)
    elif c== "-" :
        print("subtraction=", a - b) 
    elif c == "%":
        print("remainder=", a % b)
    elif c== "**":
        print("exponent of a over b=", a ** b)
    else:
        print("error invalid operation input.\n")
    print("Enter q to exit the program")
    choice=input()