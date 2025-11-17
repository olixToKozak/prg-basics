###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#3, 4, 5 (result is 6)
#5, 12, 13 (result is 30)
#7, 24, 25 (result is 84)
#
import math

def triangle_area(a, b, c):
    s=1/2(a+b+c)
    a=math.sqrt(s(s-a)(s-b)(s-c))
    return a

triangle1 = triangle_area(3, 4, 5)

print(f'The area of ​​a triangle with sides 3,4,5 is {triangle1 }')
print('The area of ​​a triangle with sides ... is ...')
print('The area of ​​a triangle with sides ... is ...')