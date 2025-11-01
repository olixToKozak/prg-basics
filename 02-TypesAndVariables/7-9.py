import random
dice=random.randint(1,6)
special=dice==1 or dice==6
print('Dice rolled:',dice)
print('Special number (1 or 6):',special)