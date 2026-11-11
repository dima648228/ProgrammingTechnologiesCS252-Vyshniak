import re

def convert_notation(expression: str) -> str:
    output = []
    stack = []

    priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    tokens = re.findall(r'\d+(?:\.\d+)?|[+/*^()-]', expression)

    #print(expression)

    for token in tokens:
        if token.replace('.', '', 1).isnumeric():
            output.append(token)

        elif token in priority:
            while (stack and stack[-1] != "(" and (token != "^" and priority.get(stack[-1], 0) >= priority[token])):
                output.append(stack.pop())

            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            
            if stack and stack[-1] == "(":
                stack.pop()

    while stack:
        output.append(stack.pop())

    return " ".join(output)

def calculate(expression) -> float:
    stack = []

    for token in expression.split():
        try:
            stack.append(float(token))
        except ValueError:
            b = stack.pop()
            a = stack.pop()

            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
            elif token == '^': stack.append(a ** b)

    return stack[0]

def run():
    expression = input("Type your expression: ").strip().replace(" ", "")

    converted = convert_notation(expression)

    print(calculate(converted))

if __name__ == '__main__':
    run()