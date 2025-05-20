x = int(input("Enter an integer number: "))

while x != 0:
    if x % 2 == 0:
        sm = (x+x) + (x+x) + (x+x) + (x+x) + (x+x)
        print(f"SUM = {sm}")
        x = int(input("Enter an integer number: "))
    elif x % 2 == 1:
        sm = (x+1) + (x+3) + (x+5) + (x+7) + (x+9)
        print(f"SUM = {sm}")
        x = int(input("Enter an integer number: "))
