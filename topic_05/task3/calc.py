import functions
import operations

while True:
    a = operations.get_number_input("Type A (or 'exit'): ")
    if a is None:
        break
    b = operations.get_number_input("Type B (or 'exit'): ")
    if b is None:
        break
    operation = operations.get_operation_input()
    if operation is None:
        break
    result = None
    if operation == "+":
        result = functions.add(a, b)
    elif operation == "-":
        result = functions.subtract(a, b)
    elif operation == "*":
        result = functions.multiply(a, b)
    elif operation == "/":
        result = functions.divide(a, b)
    if result is not None:
        print(f"Result: {result}")