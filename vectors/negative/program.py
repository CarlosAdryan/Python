n = int(input("How many numbers will you type? "))
while n > 10:
    print("MAXIMUM VALUE = 10")
    n = int(input("How many numbers will you type? "))

vet: [int] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input("Enter a number: "))

print("NEGATIVE NUMBERS:")
for i in range(0, n):
    if vet[i] < 0:
        print(f"{vet[i]}")
