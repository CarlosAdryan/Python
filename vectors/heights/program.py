n = int(input("How many people will be typed? "))
name: [str] = [0 for x in range(n)]
age: [int] = [0 for x in range(n)]
height: [float] = [0 for x in range(n)]

sm = 0
for i in range(0, n):
    print(f"Data of the {i + 1}st person:")
    name[i] = str(input("Name: "))
    age[i] = int(input("Age: "))
    height[i] = float(input("Height: "))
    sm += height[i]

countdown = 0
for i in range(0, n):
    if age[i] < 16:
        countdown += i

averageHeight = sm / n
minor = (countdown / n) * 100

print()
print(f"Average height: {averageHeight:.2f}")
print(f"People under 16 years: {minor:.1f}%")

for i in range(0, n):
    if age[i] < 16:
        print(f"{name[i]}")