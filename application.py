import math

def main():
    while True:
        print("simple calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")
        
        if choice == '6':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == '5':
            num = float(input("Enter number: "))
            if num >= 0:
                print(f"Square root: {math.sqrt(num)}")
            else:
                print("Error: Cannot take square root of negative number.")
        else:
            if choice != '6':
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
