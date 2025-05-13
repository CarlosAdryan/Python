print("Enter two numbers: ")
x = int(input())
y = int(input())

while x != y:
    if x > y:
        print("DECREASING!")
    else:
        print("GROWING!")

    print("Enter other two numbers: ")
    x = int(input())
    y = int(input())
