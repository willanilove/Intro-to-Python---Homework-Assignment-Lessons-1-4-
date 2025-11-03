# Create a calculator using functions for different operations.

def add(a, b):
    return (a + b)
print(add(5,4))

def subtract(a, b):
    return (a - b)
print(subtract(10,5))

def multiply(a, b):
    return (a * b)
print(multiply(8,8))

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    else:
        return a / b
    
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Choose operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":
        result = multiply(num1, num2)
        print(f"{num1} × {num2} = {result}")
    elif choice == "4":
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} ÷ {num2} = {result}")

    main()