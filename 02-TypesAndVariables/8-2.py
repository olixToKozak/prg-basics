###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

radius=int(input('Type in radius: '))
pi=3.14159

area=pi*radius**2
circumference=2*pi*radius

print(f"Area: {area:.2f}")
print(f'Circumference: {circumference:.2f}')