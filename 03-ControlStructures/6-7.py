#Child: under 13
#een: 13 to 19
#Adult: 20 to 64
#Senior: 65 or older

age = int(input('how old are you? '))

if age >= 65:
    print('ur a senior')
elif age >= 20:
    print('ur an adult')
elif age >= 13:
    print('ur a teen')
elif age >=1:
    print('ur a child')
else:
    print('ur not even born LMAO')