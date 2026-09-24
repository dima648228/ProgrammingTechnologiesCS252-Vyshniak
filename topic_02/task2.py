
def add(a: float, b: float) -> float:
    return a+b

def subtract(a: float, b: float) -> float:
    return a-b

def multiply(a: float, b: float) -> float:
    return a*b

def divide(a: float, b: float) -> float:
    return a/b

a: float = float(input("Enter A: "))
b: float = float(input("Enter B: "))

operation: str = str(input("Choose operation (+, -, *, /):"))

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