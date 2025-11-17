###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
fractions=0

for i in range(1,11):
    fractions=1/(fractions+i)

    print(f'1/{i} = {fractions}')