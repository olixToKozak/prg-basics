#1-2 hours: 5 PLN
#3-6 hours: 15 PLN
#Over 6 hours: 20 PLN

hours = int(input('How many hours have you been parked'))

if hours >=1 and hours <3:
    print('Your fee is 5 PLN')
elif hours >2 and hours<7 :
    print('Your fee is 15 PLN')
elif hours>6:
    print('Your fee is 20 PLN')
else:
    print('kys')