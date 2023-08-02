from datetime import datetime
ano = int(input('Qual ano você nasceu: '))
atual = datetime.today().year
idade = atual - ano
if idade <= 9:
    print('MIRIM')
elif idade <= 14 and idade > 9:
    print('INFANTIL')
elif idade <= 19 and idade > 14:
    print('JUNIOR')
else:
    print('MASTER')