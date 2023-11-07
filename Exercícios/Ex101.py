from datetime import date
def voto(ano):
    idade = date.today().year-ano
    if idade >= 16 and idade < 18 or idade > 65:
        print(f'Tem {idade} e o voto opcinal')
    elif idade > 18 and idade < 65:
        print(f'Tem {idade} e o voto é obriatorio')
    elif idade < 16:
        print(f'Tem {idade} e o voto é negado')


a = int(input('Ano nascimento: '))
voto(a)
