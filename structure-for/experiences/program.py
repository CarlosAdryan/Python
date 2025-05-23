n = int(input("How many test cases will be entered? "))

totalGuineaPigs: int = 0
totalRabbits: int = 0
totalRats: int = 0
totalFrogs: int = 0

for i in range(0, n):
    x = int(input("Number of guinea pigs: "))
    guineaPig = str(input("Guinea pig type: ")).upper()
    totalGuineaPigs += x
    if guineaPig == 'C':
        totalRabbits += x
    elif guineaPig == 'R':
        totalRats += x
    elif guineaPig == 'S':
        totalFrogs += x

rabbitPercentage = totalRabbits / totalGuineaPigs
ratPercentage = totalRats / totalGuineaPigs
frogsPercentage= totalFrogs / totalGuineaPigs

print()
print("FINAL REPORT:")
print(f"Total: {totalGuineaPigs} guinea pigs")
print(f"Total rabbits: {totalRabbits}")
print(f"Total rats: {totalRats}")
print(f"Total frogs: {totalFrogs}")
print(f"Percentage of rabbits: {rabbitPercentage * 100:.2f}")
print(f"Percentage of rats: {ratPercentage * 100:.2f}")
print(f"Percentage of frogs: {frogsPercentage * 100:.2f}")