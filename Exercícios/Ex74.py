from random import randint

while True:
    numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    print('Os valores sorteados foram: ',end='')
    for n in numeros:
        print(f'{n} ',end='')
    print(f'\nO maior valor sorteado foi {max(numeros)}')
    print(f'O menor valor digitado foi {min(numeros)}')
    if max(numeros) == min(numeros):
        break