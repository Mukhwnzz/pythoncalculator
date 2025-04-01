# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        result = num1 / num2
else:
    print("Error: Invalid operation! Please use +, -, *, or /")

# Display the result (only if no errors occurred)
if operation in ('+', '-', '*', '/') and not (operation == '/' and num2 == 0):
    print(f"{num1} {operation} {num2} = {result}")