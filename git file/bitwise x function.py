def bitwise_operation(a, b, operation):
    if operation == 'AND':
        return a & b
    elif operation == 'OR':
        return a | b
    elif operation == 'XOR':
        return a ^ b
    else:
        return "Invalid operation"

a = int(input("Enter the first number (less than or equal to 15): "))
b = int(input("Enter the second number (less than or equal to 15): "))
operation = input("Enter the desired operation (AND, OR, XOR): ")
result = bitwise_operation(a, b, operation)
print("Result: ", result)
