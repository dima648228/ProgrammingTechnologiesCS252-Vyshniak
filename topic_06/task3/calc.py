from functions import CalculatorFunctions
from operations import Operations

class CalculatorApp:
    def __init__(self):
        self.calc = CalculatorFunctions()

    def run(self):
        self.calc.write_log("Program started")
        
        while True:
            a = Operations.get_number_input("Type A (or 'exit'): ")
            if a is None:
                self.calc.write_log("User is stopped the program (exit on A typing stage).")
                break
                
            b = Operations.get_number_input("Type B (or 'exit'): ")
            if b is None:
                self.calc.write_log("User is stopped the program (exit on B typing stage).")
                break
                
            operation = Operations.get_operation_input()
            if operation is None:
                self.calc.write_log("User is stopped the program (exit on operation choose stage).")
                break
                
            result = None
            if operation == "+":
                result = self.calc.add(a, b)
            elif operation == "-":
                result = self.calc.subtract(a, b)
            elif operation == "*":
                result = self.calc.multiply(a, b)
            elif operation == "/":
                result = self.calc.divide(a, b)
                
            if result is not None:
                print(f"Result: {result}")
                self.calc.write_log(f"Completed successfully: {a} {operation} {b} = {result}")
            else:
                self.calc.write_log(f"An error was occured: {a} {operation} {b}")

app = CalculatorApp()
app.run()