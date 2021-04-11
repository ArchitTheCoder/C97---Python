num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operation: ")

if (operator == "+" or operator == "add"):
    print(f"{str(num1)} + {str(num2)} = {str(num1 + num2)}")
elif (operator == "-" or operator == "subtract"):
    print(f"{str(num1)} - {str(num2)} = {str(num1 - num2)}")
elif (operator == "*" or operator == 'x' or operator == 'multiply'):
    print(f"{str(num1)} x {str(num2)} = {str(num1 * num2)}")
elif (operator == "/" or operator == "divide"):
    print(f"{str(num1)} / {str(num2)} = {str(num1 / num2)}")
