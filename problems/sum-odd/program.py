print("Enter two numbers: ")
x = int(input())
y = int(input())

if x > y:
    trade = y
    y = x
    x = trade

odd = 0
for i in range(x+1, y):
    if i % 2 != 0:
        odd = odd + i

print(f"SUM OF THE IMPARES = {odd}")