price = int(input('Enter a price: '))
amount = int(input('How many do you want to buy? '))
discount = price * 0.75

if amount >2:
    fprice=2*price+(amount-2)*discount
    print(f'Number of products purchased: {amount}')
    print(f'Product price: {price}')
    print(f'Amount to pay: {fprice}')
else:
    fprice=price*amount
    print(f'Number of products purchased: {amount}')
    print(f'Product price: {price}')
    print(f'Amount to pay: {fprice}')