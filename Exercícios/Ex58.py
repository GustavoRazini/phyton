import random
n1 = 0
n = int(input('''Acabei de pensar em um número de 1 a 10 
Será que você conssegue acertar?
Qual seu palpite? '''))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha = random.choice(lista)


while not escolha == n and escolha> n:
    n = int(input('Mais... Tente outro número: '))
    n1 += 1
    while not escolha == n and escolha < n:
        n = int(input('Menos... Tente outro número: '))
        n1 += 1
    if escolha == n:
        print('Você acertou em {} tentativas. Parabéns!'.format(n1+1))

