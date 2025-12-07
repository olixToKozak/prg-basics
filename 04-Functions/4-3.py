###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a, b, c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
letriangl1 = triangle_area(3, 4, 5)
letriangl2 = triangle_area(5, 12, 13)
letriangl3 = triangle_area(7, 24, 25)


print(f'The area of ​​a triangle with sides 3,4,5 is {letriangl1}')
print(f'The area of ​​a triangle with sides 5 12 13 is {letriangl2}')
print(f'The area of ​​a triangle with sides 7 24 25 is {letriangl3}')