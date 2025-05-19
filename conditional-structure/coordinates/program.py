x = float(input("X value: "))
y = float(input("Y value: "))

if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
elif y == 0 and x != 0:
    print("X Axis")
elif x == 0 and y != 0:
    print("X Axis")
elif x == 0 and y == 0:
    print("Origin")