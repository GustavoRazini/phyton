galera = list()
dados = list()
maiorpeso = menorpeso = 0
resposta = ''
while resposta != 'N':
    resposta = ''
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    galera.append(dados[:])
    dados.clear()
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('-='*30)
print(f'Ao todo, você cadastrou {len(galera)} pessoa(s). ')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de ',end='')
for p in galera:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ')
print(f'O menor peso foi de {menorpeso}Kg. Peso de ',end='')
for p in galera:
    if p[1] == menorpeso:
        print(f'[{p[0]}] ',end='')
print()
