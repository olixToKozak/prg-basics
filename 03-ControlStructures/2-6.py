#Write a program that checks what number was entered from the keyboard and prints one of the messages below. Then run the program and check the following numbers:
#7, 1 ,0 ,-1 , -4
#Number ... is positive
#Number ... is negative
#Number is 0

number = int(input('Enter a number: '))

if number>=0:
    print(f'number {number} is positvie')
else:
    print(f'number {number} is negative')