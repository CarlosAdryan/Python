n = int(input("How many values will each vector have? "))

vetA: [int] = [0 for x in range(n)]
vetB: [int] = [0 for x in range(n)]
vetC: [int] = [0 for x in range(n)]

print("Enter the values of vector A: ")
for i in range(0, n):
    vetA[i] = int(input())

print("Enter the values of vector B: ")
for i in range(0, n):
    vetB[i] = int(input())

sm = 0

print("RESULTING VECTOR: ")
for i in range(0, n):
    sm = vetA[i] + vetB[i]
    print(f"{sm}")
