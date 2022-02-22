#Introduction
print("This program will find the gratest common factor of two numbers")
print("")
#user input
x=num1=int(input("What is your first number?"))
y=num2=int(input("What is your secon number?"))
while num1 != num2:
    if num1 > num2:
        num1=num1-num2
    else:
        num2=num2-num1

print("HCF of",x,"and",y,"=",num1)
