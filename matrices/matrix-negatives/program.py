n = int(input("What is the number of rows in the matrix? "))
m = int(input("How many columns of the matrix? "))

mat: [[int]] = [[0 for x in range(m)] for x in range(n)]

for i in range(0, n):
    for j in range(0, m):
        mat[i][j] = int(input(f"Element [{i}, {j}]: "))

print("NEGATIVE VALUES: ")
for i in range(0, n):
    for j in range(0, m):
        if mat[i][j] < 0:
            print(f"{mat[i][j]}")