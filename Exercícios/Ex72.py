cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'dose', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
valor = ""
while valor != "N":
    valor = ""
    num = int(input('Digite um númere entre 0 e 20: '))
    if not 0 <= num <= 20:
        continue
    print(f'Você digitou o número {cont[num]}')
    while valor != "N" and valor != "S":
        valor = str(input('Você quer continuar [S/N]: ')).strip().upper()[0]

print('FIM DO PROGRAMA')