#program for checking driving age 
age=int(input("Enter you age to check for driving:\n"))
if 100>age>18:
    print("Your age is greater than 18 and you can drive.") 

elif 7<age<18:
    print("Your age is less than 18  and you cannot drive.")

elif age<7:
    
    print("Invalid age, please enter any valid age between 7 and 100")
elif age>100:
    print("Invalid age, please enter any valid age between 7 and 100")
else:
    
    print("Your age is 18 and we cannot decide therefore you need to come here and we are checking that you can drive or not")

