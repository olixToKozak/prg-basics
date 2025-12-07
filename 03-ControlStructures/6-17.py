time24=input('Enter the time: ')
time12=0

if int(time24[0:2]) > 12 and int(time24[0:2]) <=24:
    time12=int(time24[0:2])-12
    print(f'Time in 12-hour format: {time12}{time24[2:5]}PM')
elif int(time24[0:2]) >= 1  and int(time24[0:2]) <=12:
    time12=int(time24[0:2])
    print(f'Time in 12-hour format: {time12}{time24[2:5]}AM')