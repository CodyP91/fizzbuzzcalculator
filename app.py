def add_numbers(a, b):
    # Adds two numbers and returns the result
    return a + b

def subtract_numbers(a, b):
    # Subtracts the second number from the first number and returns the result
    return a - b

def multiply_numbers(a, b):
    # Multiplies two numbers and returns the result
    return a * b

def divide_numbers(a, b):
    # Divides the first number by the second number and returns the result
    return a / b

def calculator():
    while True:
        # Displaying the calculator menu
        print("Calculator Menu:")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Addition operation
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add_numbers(num1, num2)
            print("Result: ", result)

        elif choice == '2':
            # Subtraction operation
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract_numbers(num1, num2)
            print("Result: ", result)

        elif choice == '3':
            # Multiplication operation
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multiply_numbers(num1, num2)
            print("Result: ", result)

        elif choice == '4':
            # Division operation with error handling for division by zero
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            try:
                result = divide_numbers(num1, num2)
                print("Result: ", result)
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")

        elif choice == '5':
            # Exiting the calculator
            print("Exiting the calculator.")
            break

        else:
            # Invalid choice
            print("Invalid choice. Please enter a number from 1 to 5.")

# Starting the calculator
calculator()
