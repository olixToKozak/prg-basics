###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
lenght = int(a)
b= input("b=")
width= int(b)
c=input('c=')
height=int(c)

volume=lenght*width*height
surface_area=2*(lenght*width+width*height+lenght*height)

print(f"Volume of a cuboid with sides {lenght} {width} {height} is {volume}")
print(f"Surface area of a cuboid with sides {lenght} {width} {height} is {surface_area}")
