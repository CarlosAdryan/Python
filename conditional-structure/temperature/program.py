scale = str(input("Will you enter the temperature at which scale (C/F)? ")).upper()
if scale == 'F':
    temperatureF = float(input("Enter temperature in Fahrenheit: "))
    celsius = (temperatureF - 32) * (5 / 9)
    print(f"Equivalent temperature in Celsius: {celsius:.2f}")
elif scale == 'C':
    temperatureC = float(input("Enter temperature in Celsius: "))
    fahrenheit = (temperatureC * (9 / 5)) + 32
    print(f"Equivalent temperature in Fahrenheit: {fahrenheit:.2f}")