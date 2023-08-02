ficha = list()
resposta = ''
while resposta != 'N':
    resposta = ''
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1], [nota2], [media]])
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('=-'*30)
print('Nº NOME       MÉDIA')
print('-'*20)

print('=-'*20)