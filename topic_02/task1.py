import math

def discriminant(a, b , c) -> float:
    return b*b-4*a*c

a: float = float(input("Enter A: "))
b: float = float(input("Enter B: "))
c: float = float(input("Enter C: "))

if a == 0: # рівняння не квадратне
    if b != 0:
        print("Linear equation. One root:", -c / b)
    elif c == 0:
        print("Infinite number of roots (0 = 0)")
    else:
        print("No solution")
else:
    D = discriminant(a,b,c)

    if D > 0:
        root1 = (-b + math.sqrt(D))/(2*a)
        root2 = (-b - math.sqrt(D))/(2*a)

        print("First root: ", root1)
        print("Second root: ", root2)
    elif D == 0:
        root = (-b + math.sqrt(D))/(2*a)

        print("One root only: ", root)
    else:
        print("No roots")