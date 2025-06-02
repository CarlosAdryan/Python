n = int(input("What's the order of the matrix? "))

mat: [[int]] = [[0 for x in range(n)] for x in range(n)]
positiveSum = 0
alteredMatrix = 0
count = 0

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = float(input(f"Element [{i},{j}]: "))
print()
for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] > 0:
            positiveSum += mat[i][j]
print(f"SUM OF POSITIVES: {positiveSum:.1f}")
print()

line = int(input("Choose a line: "))
print(f"CHOSEN LINE: ", end='')
for j in range(0, n):
    print(f"{mat[line][j]}", end=' ')
print()
print()

column = int(input("Choose a column: "))
print(f"CHOSEN COLUMN: ", end='')
for i in range(n):
        print(f"{mat[i][column]}", end=' ')
print()
print()

print("MAIN DIAGONAL: ", end='')
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            print(f"{mat[i][j]}", end=' ')
print()
print()

print("CHANGED ARRAY: ")
for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] < 0:
            mat[i][j] = mat[i][j] * mat[i][j]
        print(f"{mat[i][j]}", end=' ')
        count += 1
        if count % 3 == 0:
            print()
