import math

coeA = float(input("Coefficient a: "))
coeB = float(input("Coefficient b: "))
coeC = float(input("Coefficient c: "))

delta = coeB ** 2 - 4 * coeA * coeC

if coeA == 0:
    print("The value of 'a' must not be zero.")
elif delta > 0:
    x1 = (-coeB + math.sqrt(delta)) / (2 * coeA)
    x2 = (-coeB - math.sqrt(delta)) / (2 * coeA)
    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")
elif delta == 0:
    x = -coeB / (2 * coeA)
    print(f"X = {x:.4f}")
else:
    print("This equation has no real roots")

