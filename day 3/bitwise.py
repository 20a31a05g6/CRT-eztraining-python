a = int(input("Enter the first number (less than or equal to 15): "))
b = int(input("Enter the second number (less than or equal to 15): "))
operation = input("Enter the desired operation (AND, OR, XOR): ")

if operation == 'AND':
    result = a & b
elif operation == 'OR':
    result = a | b
elif operation == 'XOR':
    result = a ^ b
else:
    result = "Invalid operation"

print("Result: ", result)
