num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operation = (input("please enter for what kind of operation you want  (+,-,*,/): "))

if operation == "+":
    print("summation is : ",num1 + num2)
elif operation == "-":
    print("subtraction is : ",num1 - num2)
elif operation == "*":
    print("multiplication is : ",num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("divison is : ",num1 / num2)
    else:
        print("Error! can't divided by zero")
else:
    ("invalid operation. please enter one of =,-,*,/.")