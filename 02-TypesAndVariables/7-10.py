import random

dice=random.randint(1,6)
guess=int(input('Guess the number: '))
winner=dice<guess
print(f'You won: {winner}')