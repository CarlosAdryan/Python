print("Enter the X and Y coordinate values:")
x = int(input())
y = int(input())

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("QUADRANT Q1")
    elif x < 0 and y > 0:
        print("QUADRANT Q2")
    elif x < 0 and y < 0:
        print("QUADRANT Q3")
    elif x > 0 and y < 0:
        print("QUADRANT Q4")
    x = int(input())
    y = int(input())