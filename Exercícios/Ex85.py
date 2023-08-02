lista = [[], []]
valor = 0
for contador in range(1, 8):
    valor = int(input(f'Digite o {contador}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print('=-=-=-=-=-=-=-=-=-=-=-=')
lista[0].sort()
lista[1].sort()
print(f'Os valores PARES digitados foram: {lista[0]}')
print(f'Os valores ÍMPARES digitados foram: {lista[1]}')