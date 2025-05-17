salary = float(input("Enter the person's salary: "))

if salary <= 1000.00:
    newSalary = (salary * 0.20) + salary
    increase = (salary * 0.20)
    print(f"New salary = {newSalary:.2f}")
    print(f"Increase = R$ {increase:.2f}")
    print(f"Percentage = 20 %")
elif salary <= 3000.00:
    newSalary = (salary * 0.15) + salary
    increase = (salary * 0.15)
    print(f"New salary = {newSalary:.2f}")
    print(f"Increase = R$ {increase:.2f}")
    print(f"Percentage = 15 %")
elif salary <= 8000.00:
    newSalary = (salary * 0.10) + salary
    increase = (salary * 0.10)
    print(f"New salary = {newSalary:.2f}")
    print(f"Increase = R$ {increase:.2f}")
    print(f"Percentage = 10 %")
else:
    newSalary = (salary * 0.05) + salary
    increase = (salary * 0.05)
    print(f"New salary = {newSalary:.2f}")
    print(f"Increase = R$ {increase:.2f}")
    print(f"Percentage = 5 %")

