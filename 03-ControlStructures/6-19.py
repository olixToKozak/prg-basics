#SURVEY Are you interested in computer science? (y/n): y
#Do you like playing computer games? (y/n): n
#Do you have an Instagram account? (y/n): y

#SURVEY RESULTS Interested in computer science: Yes
#Playing computer games: No
#Has an Instagram account: Yes

cs = input('Are you interested in computer science? (y/n): ')
cg = input('Do you like playing computer games? (y/n): ')
ia = input('Do you have an Instagram account? (y/n): ')

if cs == 'y':
    print('Interested in computer science: Yes')
elif cs == 'n':
    print('Interested in computer science: no')
    
if cg == 'y':
    print('Playing computer games: Yes')
elif cg == 'n':
    print('Playing computer games: No')
    
if ia == 'y':
    print('Has an Instagram account: Yes')
elif ia == 'n':
    print('Has an Instagram account: no')
else:
    print('you are stupid')