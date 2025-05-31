n = int(input("How many rows will each matrix have? "))
m = int(input("How many columns will each matrix have? "))

a: [[int]] = [[0 for x in range(m)] for x in range(n)]
b: [[int]] = [[0 for x in range(m)] for x in range(n)]
c: [[int]] = [[0 for x in range(m)] for x in range(n)]
count = 0

print("Enter the values of the matrix A: ")
for i in range(0, n):
    for j in range(0, m):
        a[i][j] = int(input(f"Element [{i, j}]: "))

print("Enter the values of the matrix B: ")
for i in range(0, n):
    for j in range(0, m):
        b[i][j] = int(input(f"Element [{i, j}]: "))

print("SUM MATRIX: ")
for i in range(0, n):
    for j in range(0, m):
        c[i][j] = a[i][j] + b[i][j]
        print(f"{c[i][j]}", end=' ')
        count += 1
        if count % 3 == 0:
            print()