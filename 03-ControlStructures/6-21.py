pln = int(input('Enter the amount: '))
zl5=0
zl2=0
zl1=0
while pln > 0:
    if pln-5>=0:
        pln=pln-5
        zl5=zl5+1
    elif pln-2>=0:
        pln=pln-2
        zl2=zl2+1
    else:
        pln=pln-1
        zl1=zl1+1
print (f'5zl: {zl5}')
print (f'2zl: {zl2}')
print (f'1zl: {zl1}')