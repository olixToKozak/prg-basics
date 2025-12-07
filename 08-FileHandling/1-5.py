###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    number = 0
    for line in file:
        number += 1
        print(number,line, end="")