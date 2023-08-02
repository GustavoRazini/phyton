casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é seu sálario? R$'))
anos = int(input('Em quantos anos você vai pagar a casa? '))
meses = anos*12
parcela = casa/meses
minimo = salario*0.30
print('Para comprar uma casa de {:.2f} em {} ano(s) você vai precisar pagar R${:.2f} por mês.'.format(casa,anos,parcela))
if parcela<=minimo:
    print('Seu emprestimo irá ser ACEITO!')
else:
    print('Seu emprestimo irá ser NEGADO!')
