n = int(input("What's the order of the matrix? "))
mat: [[int]] = [[0 for x in range(n)] for x in range(n)]

negatives = 0

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input(f"Element [{i},{j}]: "))

print("MAIN DIAGONAL: ")
for i in range(0, n):
    for j in range(0,n):
        if i == j:
            print(f"{mat[i][j]}", end=" ")
print()
for i in range(0, n):
    for j in range(0,n):
        if mat[i][j] < 0:
            negatives += 1
print(f"AMOUNT OF NEGATIVES = {negatives}")