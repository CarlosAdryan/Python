print("Enter ages:")
sm: int = 0
typed: int = 0

ages = int(input())
if ages < 0:
    print("IMPOSSIBLE TO CALCULATE")
else:
    while ages > 0:
        sm += ages
        typed += 1
        ages = int(input())
    average = sm / typed
    print(f"AVERAGE = {average:.2f}")
