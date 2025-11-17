###
# Program for testing built-in functions
#
#the largest number: 7,5,6,3,8,2
#the smallest number: 4,7,2,3,9,8
#length of the phrase: "computer science"
#letter read from the keyboard
#number representing the string "20303"
#binary string representing decimal number 304
#hexadecimal string representing decimal number 304
#integer representing the Unicode code of the € sign
#absolute value of -17


max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

str_input = input("Enter a tring")
print("u enterd",str_input)

str_num = str(20303)
print('str',str_num)

bin_number = bin(304)
print("binary:",bin_number)

hex_number = hex(304)
print("hex:",hex_number)

int_uni = int('€')
print('Int:',int_uni)

abs_value = abs(-17)
print('Absolute value: ',abs_value)