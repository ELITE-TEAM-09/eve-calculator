def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    else:
        return a / b

def calculator():
    print("python calculator!")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

    if operation == '1':
        result = add(num1, num2)
        print(f"The sum of {num1} + {num2} is: {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"The difference of {num1} - {num2} is: {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"The product of {num1} * {num2} is: {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Invalid operation selection! Please choose a valid operation (1/2/3/4).")

if __name__ == "__main__":
    calculator()
