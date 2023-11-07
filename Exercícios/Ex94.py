pessoa = dict()
lista = list()
res = 'S'

# coleta de dados
while True:
    if res in 'Ss':
        pessoa['nome'] = str(input('Nome: '))

        # validação do sexo
        while True:
            pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
            if pessoa['sexo'] not in 'MmFf':
                print('\033[1;31mERRO! O valor digitado não esta em [M/F]... Tente novamente...\033[m')
            else:
                break

        pessoa['idade'] = int(input('Idade: '))

        # validação do res
        while True:
            res = input('Quer continuar? [S/N] ').upper()[0]
            if res not in 'SsNn':
                print('\033[1;31mERRO! O valor digitado não esta em [S/N]... Tente novamente...\033[m')
            else:
                break

        lista.append(pessoa.copy())

    elif res in 'Nn':
        break

# printar os dados na tela
# A)
print('-=' * 30)
print(f' -Foram cadastradas o total de {len(lista)} pessoas')

# B)
somaidade = 0
for i, v in enumerate(lista):
    somaidade += v['idade']
print(f' -A media das idades é igual a: {somaidade / len(lista):.1f} anos')

# C)
print(f' -As mulheres cadastradas foram: ', end='')
for i, v in enumerate(lista):
    if v['sexo'] in 'Ff':
        print(v['nome'], end=' ')
print()

# D)
print(' -pessoas com idade acima da media: ')
for i, v in enumerate(lista):
    if v['idade'] > (somaidade / len(lista)):
        for k, valor in v.items():
            print(f'  -{k} é {valor} ;', end=' ')
        print()

print('-=' * 30)
print('\033[1;32mPrograma finalizado com sucesso...')
print('Volte sempre :D\033[m')