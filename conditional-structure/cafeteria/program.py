purchasedProduct = int(input("Product code purchased: "))
quantity = int(input("Quantity purchased: "))

if purchasedProduct > 5:
    print("Product out of stock")
elif purchasedProduct == 1:
    payable = 5.00 * quantity
elif purchasedProduct == 2:
    payable = 3.50 * quantity
elif purchasedProduct == 3:
    payable = 4.80 * quantity
elif purchasedProduct == 4:
    payable = 8.90 * quantity
elif purchasedProduct == 5:
    payable = 7.32 * quantity

print(f"Amount to pay = {payable:.2f}")