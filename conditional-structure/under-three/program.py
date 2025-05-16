firstV = int(input("First value: "))
secondV = int(input("Second value: "))
thirdV = int(input("Third value: "))

if firstV < secondV and firstV < thirdV:
    print(f"MINOR = {firstV}")
elif secondV < firstV and secondV < thirdV:
    print(f"MINOR = {secondV}")
else:
    print(f"MINOR = {thirdV}")