nota1 = float(input('Digite a NOTA1: '))
nota2 = float(input('Digite a NOTA2: '))
media = (nota1+nota2)/2
if media<5:
    print('REPROVADO')
elif media>7:
    print('APROVADO')
else:
    print('RECUPERÇÃO')