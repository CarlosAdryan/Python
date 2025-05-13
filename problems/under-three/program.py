a = int(input("First value: "))
b = int(input("Second value: "))
c = int(input("Third value: "))

if a < b and a < c:
    print(f"MINOR = {a}")
elif b < c:
    print(f"MINOR = {b}")
else:
    print(f"MINOR = {c}")