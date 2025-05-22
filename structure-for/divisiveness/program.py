n = int(input("How many cases will you type? "))

for i in range(0, n):
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("IMPOSSIBLE DIVISION")
    elif denominator != 0:
        division = numerator / denominator
        print(f"DIVISIVENESS = {division:.2f}")
