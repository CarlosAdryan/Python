fuelType = int(input("Enter a code (1, 2, 3) or 4 to stop: "))

alcohol: int = 0
petrol: int = 0
diesel: int = 0

while fuelType != 4:
    if fuelType == 1:
        alcohol += 1
    elif fuelType == 2:
        petrol += 1
    elif fuelType == 3:
        diesel += 1
    fuelType = int(input("Enter a code (1, 2, 3) or 4 to stop: "))

print("THANKS A LOT" )
print(f"Alcohol: {alcohol}")
print(f"Petrol: {petrol}")
print(f"Diesel: {diesel}")

