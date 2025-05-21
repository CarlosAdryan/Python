n = int(input("How many numbers will you type? "))

for i in range(0, n):
    x = int(input("Enter a number: "))
    if x % 2 != 0 and x < 0:
        print("NEGATIVE IMPAIRMENT")
    elif x % 2 != 0 and x > 0:
        print("POSITIVE IMPAIRMENT")
    elif x % 2 == 0 and x < 0:
        print("NEGATIVE PAIR")
    elif x % 2 == 0 and x > 0:
        print("POSITIVE PAIR")
    elif x == 0:
        print("NULL")