unitPrice = float(input("Product unit price: "))
quantity = int(input("Quantity purchased: "))
received = float(input("Money received: "))

subtotal = unitPrice * quantity

change = subtotal - received

if received < subtotal:
    print(f"INSUFFICIENT MONEY. {change:.2f} REAIS ARE MISSING")
else:
    print(f"CHANGED = {change:.2f}")
