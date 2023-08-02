valor = list()
resp = ''
while resp != 'N':
    resp = ''
    v = int(input('Digite um valor: '))
    if v not in valor:
        valor.append(v)
        print('Valor adicionado...')
    elif v in valor:
        print('Valor duplicado...')
    while resp != 'N' and resp != 'S':
        resp = str(input('Você quer continuar [S/N]: ')).strip().upper()[0]
print('-='*30)
valor.sort()
print(f'Você digitou o(s) valor(es) {valor}')
print('FIM DO PROGRAMA')