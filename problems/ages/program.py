print("First person data: ")
name1 = input("Name: ")
age1 = int(input("Age: "))
print("Second person data: ")
name2 = input("Name: ")
age2 = int(input("Age: "))

average = (age1 + age2) / 2

print(f"The average age of {name1} and {name2} is {average:.1f} years")