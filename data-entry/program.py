salary1: float; salary2: float
name1: str; name2: str
age: int
sex: str

name1 = input("First person's name: ")
salary1 = float(input("First person salary: "))

name2 = input("Second person's name: ")
salary2 = float(input("Second person salary: "))

age = int(input("Enter an age: "))
sex = input("Type a sex (F/M): ")

print(f"Name 1: {name1}")
print(f"Salary 1: {salary1:.2f}")
print(f"Name 2: {name2}")
print(f"Salary 2: {salary2:.2f}")
print(f"Age: {age}")
print(f"Sex: {sex}")