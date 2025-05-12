import math

base = float(input("Rectangle base: "))
height = float(input("Rectangle height: "))

area = base * height
perimeter = 2 * (base + height)
diagonal = math.sqrt((height * height) + (base * base))

print(f"AREA = {area:.4f}")
print(f"PERIMETER = {perimeter:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
