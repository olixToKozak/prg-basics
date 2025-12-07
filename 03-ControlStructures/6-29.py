number = int(input('Enter a number: '))
total=''
for i in range(2,number+1):
    if i != 2 and i != 3:
        if i % 2 != 0 and i % 3 != 0 and i % 5 !=0:
            total+=str(i)+' '
    else:
        total+=str(i)+' '
print(total)