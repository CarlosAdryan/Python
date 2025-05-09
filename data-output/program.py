age: int
salary: float
name: str
sex: str

age = 32
salary = 4560.9
name = "Maria Silva"
sex = "F"

print(f"{name}, sex {sex}, wins {salary:.2f}, and is {age} years old")

print("{:s}, sex {:s}, wins {:.2f}, and is {:d} years old".format(name, sex, salary, age))