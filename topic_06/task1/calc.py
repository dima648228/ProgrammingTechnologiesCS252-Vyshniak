import functions
import operations

def write_log(message: str):
    with open("calc_logs.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

write_log("Program started")

while True:
    a = operations.get_number_input("Type A (or 'exit'): ")
    if a is None:
        write_log("User is stopped the program (exit on A typing stage).")
        break

    b = operations.get_number_input("Type B (or 'exit'): ")
    if b is None:
        write_log("User is stopped the program (exit on B typing stage).")
        break

    operation = operations.get_operation_input()
    if operation is None:
        write_log("User is stopped the program (exit on operation choose stage).")
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
        write_log(f"Completed successfully: {a} {operation} {b} = {result}")
    else:
        write_log(f"An error was occured: {a} {operation} {b}")