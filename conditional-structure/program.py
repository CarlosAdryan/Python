hour: int

hour = int(input("Enter a day hour: "))

if hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
else:
    print("Good night")