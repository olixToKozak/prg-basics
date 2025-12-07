cpin='0805'
tries=3
while tries>0:
    pin=input('Enter the pin: ')
    if pin!=cpin:
        tries=tries-1
        print(f'incorrect you have {tries} left')
    else:
        print('correct')
        break
print('no tries left')
        

        