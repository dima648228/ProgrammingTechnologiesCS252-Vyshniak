def discriminant(a, b , c) -> str:
    result = b*b-4*a*c

    if discriminant < 0:
        return "No roots"
    
    return str(result)

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

result = discriminant(a,b,c)
print(result)