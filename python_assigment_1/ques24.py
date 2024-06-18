# simple calculator
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
op=input("Enter the operation you would like to perform: ")
if op=='+':
    print("Sum:",num1+num2)
elif op=='-':
    print("Difference:",num1-num2)
elif op=='*':
    print("Product:",num1*num2)
elif op=='/':
    print("Result:",num1/num2)
else:
    print("Operator not defined")