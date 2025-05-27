n = int(input("How many students will be typed? "))

name: [str] = [0 for x in range(n)]
sem1: [float] = [0 for x in range(n)]
sem2: [float] = [0 for x in range(n)]
average: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Enter name, first and second grade of the {i}st student: ")
    name[i] = input()
    sem1[i] = float(input())
    sem2[i] = float(input())
    average[i] = (sem1[i] + sem2[i]) / 2

print("Students approved: ")
for i in range(0, n):
    if average[i] >= 6.0:
        print(f"{name[i]}")