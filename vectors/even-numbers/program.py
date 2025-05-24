n = int(input("How many numbers will you type? "))

vet: [int] = [0 for x in range(n)]
pairs: [int] = [0 for x in range(n)]
sm = 0

for i in range(0, n):
    vet[i] = int(input("Enter a number: "))
    if vet[i] % 2 == 0:
        pairs[i] = vet[i]
        sm += 1
print()
print("PAIRS:")
for i in range(0, n):
    if pairs[i] != 0:
        print(f"{pairs[i]}", end="  ")
print()
print()
print(f"PAIRS QUANTITY = {sm}")