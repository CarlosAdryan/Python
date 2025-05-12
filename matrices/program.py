M = int(input("How many line will the matrix have? "))
N = int(input("How many columns will the matrix have? "))

mat: [[int]] = [[0 for x in range(N)] for x in range(M)]

for i in range(0, M):
    for j in range(0, N):
        mat[i][j] = int(input(f"Element [{i},{j}]: "))

print()
print("TYPED MATRIX:")
for i in range(0,M):
    for j in range(0,N):
        print(f"{mat[i][j]} ", end="")
    print()
