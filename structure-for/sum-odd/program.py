print("Enter two numbers: ")
x = int(input())
y = int(input())

if x > y:
    trade = x
    x = y
    y = trade

sm: int = 0
for i in range(x + 1, y):
    if i % 2 != 0:
        sm = sm + i
print(f"SUM OF THE IMPARES = {sm}")