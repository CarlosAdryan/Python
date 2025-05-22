n = int(input("How many cases will you type? "))

for i in range (0, n):
    print("Enter three numbers:")
    a = float(input())
    b = float(input())
    c = float(input())
    a = a * 2
    b = b * 3
    c = c * 5
    average = (a + b + c) / 10
    print(f"AVERAGE = {average:.1f}")