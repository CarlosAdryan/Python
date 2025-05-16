print("Enter three distances: ")
distance1 = float(input())
distance2 = float(input())
distance3 = float(input())

if distance1 > distance2 and distance1 > distance3:
    print(f"LONGER DISTANCE = {distance1:.2f}")
elif distance2 > distance1 and distance2 > distance3:
    print(f"LONGER DISTANCE = {distance2:.2f}")
else:
    print(f"LONGER DISTANCE = {distance3:.2f}")