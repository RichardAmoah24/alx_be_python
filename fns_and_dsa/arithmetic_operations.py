# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    # Convert inputs to proper types
    num1 = float(num1)
    num2 = float(num2)
    operation = str(operation).strip().lower()  # Normalize the input

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            result = "Error: Division by zero is not allowed"
        else:
            result = num1 / num2
    else:
        result = "Error: Invalid operation"

    return result


# Make the script executable on its own
if __name__ == "__main__":
    print("Arithmetic Operations")
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input(
        "Enter the operation (add, subtract, multiply, divide): ")

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")
