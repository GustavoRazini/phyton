from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('      JOGA NA MEGA SENA')
print('-'*30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quantidade:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
            if count >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'SORTEANDO {quantidade} JOGO(S)', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('-='*5, '< BOA SORTE! >', '-='*5)
