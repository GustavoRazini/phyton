import random
from time import sleep
n = int(input('What is your guess?: '))

list = [0, 1, 2, 3, 4, 5]
choosen = random.choice(list)
print('The number is {}'.format(choosen))

print('LOADING...')
sleep(3)

if n == choosen:
    print('You win! CONGRATULATIONS!')
else:
    print('You have failed, try again!')

