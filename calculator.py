# Function to perform arithmetic operations
def calculate(x, y, operation):
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        if x != 0:
            return x / y
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation."

# Prompt user for input
print("Welcome")
x = float(input("Enter the first num: "))
y = float(input("Enter the second num: "))

print("Choose an operation:")
print(" Add")
print(" Subtract")
print(" Multiply")
print(" Divide")

operation_choice = input("Enter the operation (add, subtract, multiply, divide): ").lower()

# Perform the calculation and display the result
result = calculate(x, y, operation_choice)
print(f"The result of {operation_choice}ing {x} and {y} is: {result}")
