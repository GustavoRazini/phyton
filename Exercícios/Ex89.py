ficha = list()
resposta = ''
while resposta != 'N':
    resposta = ''
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], [media]])
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('=-'*23)
print(f'{"Nº":<4} {"NOME":<10} {"MÉDIA":>8}')
for indice, aluno in enumerate(ficha):
    print(f'{indice}    {aluno[0]}             {aluno[2]}')
while True:
    print('-'*46)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

