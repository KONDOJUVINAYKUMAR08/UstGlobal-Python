import tempConversion

cel=float(input("Enter the temperature in celsius: "))
print("Fahrenheit temp: ", tempConversion.ctof(cel))
fah=float(input("Enter the temperature in fahrenheit: "))
print(f"Celsius temp: {tempConversion.ftoc(fah):.2f}")