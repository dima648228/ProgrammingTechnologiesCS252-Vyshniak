
def add(a: float, b: float) -> float:
    return a+b

def subtract(a: float, b: float) -> float:
    return a-b

def multiply(a: float, b: float) -> float:
    return a*b

def divide(a: float, b: float) -> float | None:
    try:
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

def get_number_input(prompt: str) -> float | None:
    while True:
        user_input = input(prompt).strip()

        if user_input.lower() == "exit":
            return None

        try:
            return float(user_input)
        except ValueError:
            print("This input is incorrect")

def get_operation_input() -> str | None:
    valid_operations = {"+", "-", "*", "/"}
    while True:
        operation = input("Choose operation (+, -, *, /): ").strip()

        if operation.lower() == "exit":
            return None

        if operation in valid_operations:
            return operation

        print("Invalid operation")

while True:
    a = get_number_input("Type A (or 'exit'): ")
    if a is None:
        break

    b = get_number_input("Type B (or 'exit'): ")
    if b is None:
        break

    operation = get_operation_input()
    if operation is None:
        break

    result = None
    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)

    if result is not None:
        print(f"Result: {result}")