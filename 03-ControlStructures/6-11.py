price1 = int(input('Enter previus price of the product: '))
price2 = int(input('Enter current price of the  product: '))

discount = (price1-price2)/price1*100

if discount >= 10:
    print(discount)
    print(f'current price: {price2}')
    print(f'previos price: {price1}')
    print(f'Buy the product!!')
    print(f'Product price reduced by {discount}%')
else:
    print('dont buy')

