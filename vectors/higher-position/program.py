n = int(input("How many numbers will you type? "))

vet: [float] = [0 for x in range(n)]

bigger = 0
position = 0

for i in range(0, n):
    vet[i] = float(input("Enter a number: "))
    if vet[i] > bigger:
        bigger = vet[i]
        position = i

print()
print(f"HIGHEST VALUE = {bigger}")
print(f"POSITION OF THE HIGHEST VALUE = {position}")