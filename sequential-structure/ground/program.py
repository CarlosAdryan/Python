width = float(input("Enter the width of the land: "))
length = float(input("Enter the length of the terrain: "))
value = float(input("Enter the value of the square meter: "))

area = width * length
price = area * value

print(f"Land area = {area:.2f}")
print(f"Land price = {price:.2f}")
