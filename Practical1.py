import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    discriminantSqrt = math.sqrt(discriminant)
    firstRoot = (-b + discriminantSqrt) / (2 * a)
    secondRoot = (-b - discriminantSqrt) / (2 * a)
    print(firstRoot, secondRoot)
elif discriminant == 0:
    discriminantSqrt = math.sqrt(discriminant)
    root = (-b + discriminantSqrt) / (2 * a)
    print(root)
else:
    print("Quadratic Equation has complex roots")
