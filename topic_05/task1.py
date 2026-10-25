import random

CHOICES = {
    1: "stone",
    2: "scissors",
    3: "paper"
}

RULES = {
    "stone": "scissors",
    "scissors": "paper",
    "paper": "stone"
}

running = True
while running:
    choice = input("Type your value ('stone', 'scissors' or 'paper') or 'exit': ")

    if choice == "exit":
        break

    if choice not in RULES:
        print("Invalid choice! Try again\n")
        continue

    pc_choice = CHOICES[random.randint(1, len(CHOICES))]
    print(f"PC chose: {pc_choice}")

    if choice == pc_choice:
        print("Result: Draw!\n")
    elif RULES[choice] == pc_choice:
        print("Result: You win!\n")
    else:
        print("Result: You lose!\n")
    