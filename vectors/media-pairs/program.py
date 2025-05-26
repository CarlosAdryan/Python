n = int(input("How many elements will the vector have? "))

vet: [int] = [0 for x in range (n)]

sm = 0
count = 0

for i in range(0, n):
    vet[i] = int(input("Enter a number: "))
    if vet[i] % 2 == 0:
        sm += vet[i]
        count += 1

if vet[i] % 2 == 0:
    pairsAverage = sm / count
    print(f"PAIRS AVERAGE = {pairsAverage}")
else:
    print("NO NUMBER PAIR ")