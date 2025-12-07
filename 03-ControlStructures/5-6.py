###
# Calculates the sum of even numbers from 1 to a given number N
#
count=0
N = 10
sum_even = 0

# Calculate the sum of even numbers
while count <N:
    count +=1
    if count % 2 == 0:
        sum_even += count
print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
