n = int(input("What's the order of the matrix? "))

diagonalSum = 0
col = 0

mat: [[int]] = [[0 for x in range(n)] for x in range(0, n)]
for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input(f"Element [{i,j}]: "))

for i in range(0, n):
    for j in range(1, n):
        col = j + i
        if col < n:
            diagonalSum += mat[i][col]

print(f"SUM OF THE ELEMENTS ABOVE THE MAIN DIAGONAL = {diagonalSum}")