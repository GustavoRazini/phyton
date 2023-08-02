from random import randint
c = 0
print('=-'*12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*12)

while True:
    n = int(input('Digite um valor: '))
    pi = ' '
    nc = randint(1, 10)
    soma = nc + n
    while pi not in 'PI':
        pi = str(input('PAR ou ÍMPAR? (P/I) ')).strip().upper()[0]
    print('=-' * 12)
    print(f'Você jogou {n} e o computador {nc}. Total de {soma} ',end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if soma % 2 == 0 and pi == 'I':
        print('Você Perdeu!')
        break
    elif soma % 2 == 1  and pi == 'P':
        print('Você Perdeu!')
        break
    elif soma % 2 == 1 and pi == 'I':
        print('Você Venceu!')
        c += 1
    elif soma % 2 == 0 and pi == 'P':
        print('Você Venceu!')
        c += 1
print('=-'*12)
print(f'Você venceu {c} concecutivas')
