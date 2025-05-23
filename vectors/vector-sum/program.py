n = int(input("How many numbers will you type? "))

vet: [int] = [0 for x in range(n)]

sm: float = 0
average: float = 0
for i in range(0, n):
    vet[i] = float(input("Enter a number: "))
    sm += vet[i]

print()

print("VALUES = ", end="")
for i in range(0, n):
    print(f"{vet[i]:.1f}", end=" ")
average = sm / n
print()
print(f"SUM = {sm:.2f}")
print(f"AVERAGE = {average:.2f}")