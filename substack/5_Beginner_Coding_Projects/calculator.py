def calculator():
    while True:
        operation = input("Choose an operation (+, -, *, /) or 'q' to quit: ")
        
        if operation.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        
        if operation not in ('+', '-', '*', '/'):
            print("Invalid operation. Please choose a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero")
                continue
        
        print(f"Result: {result}")

calculator()
