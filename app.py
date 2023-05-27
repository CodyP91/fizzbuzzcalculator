def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b

def calculator():
    while True:
        print("Calculator Menu:")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add_numbers(num1, num2)
            print("Result: ", result)
            
        elif choice == '2':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract_numbers(num1, num2)
            print("Result: ", result)
            
        elif choice == '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multiply_numbers(num1, num2)
            print("Result: ", result)
            
        elif choice == '4':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            try:
                result = divide_numbers(num1, num2)
                print("Result: ", result)
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
            
        elif choice == '5':
            print("Exiting the calculator.")
            break
            
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

calculator()