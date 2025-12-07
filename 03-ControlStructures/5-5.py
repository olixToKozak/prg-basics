###
# Sums numbers entered by user
#
total_sum = 0
total_inputs = 0
aritmetic = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    total_inputs += 1
    aritmetic = total_sum/total_inputs 

print(f"The total sum of the numbers is: {total_sum}")
print(f"Arithmetic mean of the numbers is: {aritmetic}")