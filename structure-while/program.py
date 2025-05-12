x: int
s: int

s = 0
x = int(input("Enter first number: "))

while x != 0:
    s = s + x
    x = int(input("Enter another number: "))

print("SUM = ", s)