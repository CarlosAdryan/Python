n = int(input("How many people will be typed? "))

height: [float] = [0 for x in range(n)]
genre: [str] = [0 for x in range(n)]

minor = 0
bigger = 0
averageWomen = 0
womenSum = 0
typedWomen = 0
typedMen = 0

for i in range(0, n):
    height[i] = float(input(f"Height of the {i}st person: "))
    genre[i] = (input(f"Genre of the {i}st person: ")).upper()
    minor = height[0]
    if height[i] > bigger:
        bigger = height[i]
    if genre[i] == "F":
        typedWomen += 1
        womenSum += height[i]
    elif genre[i] == "M":
        typedMen += 1

for i in range(0, n):
    if height[i] < minor:
        minor = height[i]

averageWomen = womenSum / typedWomen
print(f"Lower height = {minor}")
print(f"Higher height = {bigger}")
print(f"Women's heights average = {averageWomen:.2f}")
print(f"Number of men = {typedMen}")

