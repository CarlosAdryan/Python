password = int(input("Enter password: "))

while password != 2002:
    password = int(input("Invalid Password! Try again: "))
if password == 2002:
    print("Access allowed!")
