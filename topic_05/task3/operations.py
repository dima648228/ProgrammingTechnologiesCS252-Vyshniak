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