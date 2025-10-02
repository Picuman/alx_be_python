def perform_operation(num1, num2, operation):
    operation = operation.strip().lower()
    
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError("Unsupported operation. Please use '+', '-', '*', or '/'.")


