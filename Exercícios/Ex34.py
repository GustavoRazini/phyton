salario = float(input('Qual é seu salário? '))
if salario <= 1250:
    novo = salario*1.15
else:
    novo = salario*1.10
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,novo))