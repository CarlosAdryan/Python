minutes = int(input("Enter the amount of minutes: "))
payable = 50.00

if minutes > 100:
    payable = payable + 2 * (minutes - 100)

print(f"Amount payable: R$ {payable:.2f}")