print("Enter two whole numbers: ")
a = int(input())
b = int(input())

if a < b:
    trade = b
    b = a
    a = b

if a % b == 0:
    print("Are multiple")
else:
    print("They're not multiplies")