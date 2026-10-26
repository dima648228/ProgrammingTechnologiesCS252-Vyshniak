class CalculatorFunctions:
    def __init__(self, log_filename: str = "calc_logs.txt"):
        self.log_filename = log_filename

    def write_log(self, message: str):
        with open(self.log_filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float | None:
        try:
            return a / b
        except ZeroDivisionError:
            print("Cannot divide by zero")
            return None