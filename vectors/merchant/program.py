n = int(input("How many products data will be entered? "))

names: [str] = [0 for x in range(n)]
purchasePrice: [float] = [0 for x in range(n)]
salesPrice: [float] = [0 for x in range(n)]
average: [float] = [0 for x in range(n)]

totalPurchase = 0
totalSale = 0
totalProfit = 0

below = 0
between = 0
above = 0

for i in range(0, n):
    print(f"Product {i + 1}:")
    names[i] = input("Name: ")
    purchasePrice[i] = float(input("Purchase price: "))
    salesPrice[i] = float(input("Sales price: "))
    average[i] = (salesPrice[i] - purchasePrice[i]) / purchasePrice[i] * 100
    totalPurchase += purchasePrice[i]
    totalSale += salesPrice[i]
    totalProfit = totalSale - totalPurchase

print("REPORT:")

for i in range(0, n):
    if average[i] < 10.00:
        below += 1
    elif 10.00 <= average[i] <= 20.00:
        between += 1
    elif average[i] > 20.00:
        above += 1

print(f"Profit below 10%: {below}")
print(f"Profit between 10% and 20%: {between}")
print(f"Profit above 20%: {above}")
print(f"Total purchase amount: {totalPurchase:.2f}")
print(f"Total sale value: {totalSale:.2f}")
print(f"Total profit: {totalProfit:.2f}")