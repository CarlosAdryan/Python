N = int(input("What's the order of the matrix? "))

mat: [[int]] = [[0 for x in range(N)] for x in range(N)]

s = 0
for i in range(0, N):
    for j in range(0, N):
        mat[i][j] = int(input(f"Element [{i},{j}]: "))
        if mat[i][j] < 0:
            s = s + 1

print("DIAGONAL MAIN: ")
for i in range(0, N):
    print(f"{mat[i][i]} ", end="")
print()
print(f"NEGATIVE AMOUNT = {s}")