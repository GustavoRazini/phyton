from datetime import datetime
atual = datetime.today().year
ano = int(input('Qual ano você nasceu? '))
idade = atual-ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo1 = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo1))
else:
    saldo2 = idade - 18
    print('Você deveria ter se alistado há {} anos'.format(saldo2))