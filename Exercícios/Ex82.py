lista = list()
pares = list()
impar = list()
resp = ''
while resp != 'N':
    resp = ''
    numero = int(input('Digite um número: '))
    lista.append(numero)

    while resp != 'S' and resp != 'N':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]

for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impar.append(valor)
print('=-'*30)
print(f'''A lista completa é {lista}
A lista de pares é {pares}
A lista de ímpares é {impar} ''')