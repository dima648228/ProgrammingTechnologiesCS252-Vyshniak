
def add(a: float, b: float) -> float:
    return a+b

def subtract(a: float, b: float) -> float:
    return a-b

def multiply(a: float, b: float) -> float:
    return a*b

def divide(a: float, b: float) -> float:
    return a/b

while True:
    a: str = input("Enter A (or 'exit'): ")

    if a.lower() == "exit":
        break

    b: str = input("Enter B: ")
    operation: str = input("Choose operation (+, -, *, /):")

    a = float(a)
    b = float(b)

    if operation == "+":
        print(add(a,b))
    elif operation == "-":
        print(subtract(a,b))
    elif operation == "*":
        print(multiply(a,b))
    elif operation == "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print(divide(a,b))
    else:
        print("Unknown operation")