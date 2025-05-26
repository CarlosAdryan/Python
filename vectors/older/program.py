n = int(input("How many people are you going to type? "))

name: [str] = [0 for x in range(n)]
age: [int] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Data of the {i+1}st person:")
    name[i] = input("Name: ")
    age[i] = int(input("Age: "))

bigger = 0
older: str
for i in range(0, n):
    if age[i] > bigger:
        bigger = age[i]
        older = name[i]

print(f"OLDER PERSON: {older}")