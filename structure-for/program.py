N: int; i: int; x: int; s: int

N = int(input("How many numbers will be entered? "))

s = 0
for i in range(0, N):
    x = int(input("Enter a number: "))
    s = s + x

print("SUM = ", s)