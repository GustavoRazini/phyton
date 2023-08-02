dias = int(input('Quantos dias foram alugados? '))
km = float(input('Quantos Km foram rodados? '))
pago = (dias*60)+(km*0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
