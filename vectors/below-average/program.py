n = int(input("How many elements will the vector have? "))

vet: [float] = [0 for x in range(n)]

smTotal = 0
for i in range(0, n):
    vet[i] = float(input("Enter a number: "))
    smTotal += vet[i]

print()
vectorMedia = smTotal / n
print(f"VECTOR MEDIA = {vectorMedia}")
print("BELOW AVERAGE ELEMENTS: ")
for i in range(0,n):
    if vet[i] < vectorMedia:
        print(f"{vet[i]}")