firstNote = float(input("Enter the first note: "))
while firstNote < 0 or firstNote > 10.0:
    firstNote = float(input("Valor invalid! Try again: "))

secondNote = float(input("Enter the second note: "))
while secondNote < 0 or secondNote > 10.0:
    secondNote = float(input("Valor invalid! Try again: "))

average = (firstNote + secondNote) / 2
print(f"AVERAGE = {average:.2f}")