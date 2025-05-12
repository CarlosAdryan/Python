N = int(input("How many numbers will you type? "))

vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Enter a number: "))
print()
print("NUMBERS ENTERED:")
for i in range(0, N):
    print(f"{vet[i]:.1f}")