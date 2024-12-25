def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Floor Division")

    while True:
        # Get user input
        choice = input("Enter the number of the operation you want to perform (1-7) or 'q' to quit: ")
        
        if choice.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
            elif choice == '5':
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            elif choice == '6':
                print(f"Result: {num1} ** {num2} = {num1 ** num2}")
            elif choice == '7':
                if num2 != 0:
                    print(f"Result: {num1} // {num2} = {num1 // num2}")
                else:
                    print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice! Please select a number between 1 and 7 or 'q' to quit.")

if __name__ == "__main__":
    calculator()