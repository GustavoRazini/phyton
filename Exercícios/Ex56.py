somaidade = 0
media = 0
idadevelho =0
nomevelho = ''
mulheresmenos20 = 0

for p in range (1,5):
    print('-'*7,'{}ª PESSOA'.format(p),'-'*7)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (m)masculino (f)feminino: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Mm'and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresmenos20 += 1


media = somaidade/4
print('A média das idades é {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(idadevelho,nomevelho))
print('No total tem {} mulheres com menos de 20 anos'.format(mulheresmenos20))