n = int(input("What is the number of rows in the matrix? "))
m = int(input("How many columns of the matrix? "))

mat: [[float]] = [[0 for x in range(m)] for x in range(n)]
vet: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Enter the elements of the {i + 1}st line:")
    for j in range(0, m):
        mat[i][j] = float(input())
        vet[i] += mat[i][j]

print("GENERATED VECTOR:")
for i in range(0, n):
    print(f"{vet[i]}")