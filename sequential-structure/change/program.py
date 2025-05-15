price = float(input("Unit price of the product: "))
quantity = int(input("Quantity purchased: "))
received = float(input("Money received: "))

change = received - price * quantity

print(f"CHANGE = {change:.2f}")

