n = int(input("How many numbers will you type? "))

inside: int = 0
outside: int = 0

for i in range(0, n):
    x = int(input("Enter a number: "))
    if x % 2 != 0:
        inside += 1
    else:
        outside += 1
print(f"{inside} INSIDE")
print(f"{outside} OUTSIDE")