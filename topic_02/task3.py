
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

match operation:
    case "+":
        print(add(a,b))
    case "-":
        print(subtract(a,b))
    case "*":
        print(multiply(a,b))
    case "/" if b == 0:
        print("Cannot divide by zero")
    case "/":
        print(divide(a,b))
    case _:
        print("Unknown operation")