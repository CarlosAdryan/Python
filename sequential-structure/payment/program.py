name = str(input("Name: "))
valueHour = float(input("Value per hour: "))
hoursWorked = float(input("Hours worked: "))

payment = valueHour * hoursWorked

print(f"The payment for {name} should be {payment:.2f}")