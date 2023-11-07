from datetime import datetime
pessoa = dict()
resp = ''
while resp != 'N':
    resp = ''
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Ano nascimento: '))
    pessoa['ctps'] = int(input('CTPS: '))
    if pessoa['ctps'] == 0:
        print('-=' * 30)
        print(f'''nome tem o valor {pessoa["nome"]}
idade tem o valor {2023 - pessoa["idade"]}
ctps tem o valor {pessoa["ctps"]}''')
    else:
        pessoa['contrato'] = int(input('Ano contratação: '))
        pessoa['salario'] = float(input('Salário: R$'))
        print('-='*30)
        print(f'''nome tem o valor {pessoa["nome"]}
idade tem o valor {2023- pessoa["idade"]}
ctps tem o valor {pessoa["ctps"]}
salário tem o valor {pessoa["salario"]}
aposentadoria tem o valor {pessoa["contrato"]}''')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-='*30)
print('FIM DO PROGRAMA!')
