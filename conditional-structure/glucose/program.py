measure = float(input("Enter glucose measurement: "))

if measure <= 100:
    print("Classification: normal")
elif measure <= 140:
    print("Classification: high")
else:
    print("Classification: diabetes")