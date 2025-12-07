ean=input('Enter the EAN code: ')

if len(ean)==13:
    print('Article number is correct')
    if ean[0:3] == '590':
        print('Article manufactured in Poland')
else:
    print('incorect')        