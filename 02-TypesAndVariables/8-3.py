###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius=float(input('Type in temerature in degrees Celsius: '))

kelvin=celsius+273.15
fahrenheit=(celsius*9/5)+35

print(f'celsius {celsius:.2f}')
print(f'Kelvin {kelvin:.2f}')
print(f'Fahrenheit {fahrenheit:.2f}')