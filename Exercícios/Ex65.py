media = mediaa = c = maior = menor = 0
resp = 's'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    c += 1
    media += num
    mediaa = media/c
    if c == 1:
        maior = menor = num
    elif num > maior:
            maior = num
    elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
print('''A média entre todos os {} números digitados é {}
O Maior número é {} 
O Menor número é {}'''.format(c,mediaa,maior,menor))