n = int(input("Enter the value of N: "))

while n > 15:
    n = int(input("Enter the value of N: "))

fat = 1
for i in range (1, n + 1):
    fat *= i
print(f"{fat}")