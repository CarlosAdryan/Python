N = int(input("How many numbers will you type? "))

vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Enter a number: "))

print()
print("VALUES = ", end="")
for i in range(0, N):
    print(f"{vet[i]:.1f}", end=" ")
print()

s = 0
for i in range(0, N):
    s = s + vet[i]

print(f"SUM = {s:.2f}")

average = s / N
print(f"AVERAGE = {average:.2f}")