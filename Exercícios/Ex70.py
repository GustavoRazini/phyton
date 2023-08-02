total = totmil = menorpreco = c = 0
barato = ''
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    c += 1
    if preco > 1000:
        totmil += 1
    if c == 1 or preco < menorpreco:
        menorpreco = preco
        barato = prod
    resp = ''
    while resp != 'N':
        resp = ''
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    print('{:-^40}'.format(' FIM DO PROGRAMA '))
    print(f'O total da compra foi R${total:.2f}')
    print(f'Temos {totmil} produtos custando mais de R$1000')
    print(f'O produto mais barato foi {barato} que custa R${menorpreco:.2f}')


