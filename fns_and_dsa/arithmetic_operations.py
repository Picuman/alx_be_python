def perform_operation(num1, num2, operation):
    operation = operation.strip().lower()
    
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
           print("division by zero is impossible")
    else:
        return "Invalid operation"


num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation(add ,substract ,multiply,divide):")
result = perform_operation(num1,num2,operation)

