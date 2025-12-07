###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0

while True:
    print('')
    print('')
    print('')
    print('Which light bulb do you want to turn on?')
    print('')
    print('1. First light bulb')
    print('2. The other two')
    print('3. Check how mane are on')
    print('4. Exit')
    print('')

    choise = input('')
    if choise == '1':
        if light_switch1 == False:
            bulbs_on += 1
            light_switch1=True
            print('You turned on one light bulb')
        else:
            bulbs_on -= 1
            light_switch1=False
            print('You turned off one light bulb')
    elif choise == '2':
        if light_switch2 == False:
            bulbs_on +=2
            light_switch2=True
            print('You turned on two light bulbs')
        else:
            bulbs_on -=2
            light_switch2=False
            print('You turned off two light bulbs')
    elif choise == '3':
        print(f'there are {bulbs_on} bulbs on')
    elif choise == '4':
        break
    else:
        print('Please enter 1-4')
    