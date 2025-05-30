n = int(input("What's the order of the matrix? "))

mat: [[int]] = [[0 for x in range(n)] for x in range(n)]
bigger = 0

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input(f"Element [{i},{j}]: "))

print("LARGEST ELEMENT OF EACH LINE: ")
for i in range(0, n):
    bigger = mat[i][0]
    for j in range(0, n):
        if mat[i][j] > bigger:
            bigger = mat[i][j]
    print(f"{bigger}")
