print('-'*10,'LOJAS RZ','-'*10)
preco = float(input('Qual é o preço do produto? R$'))
avista = preco*0.90
cartao = preco*0.95
xdois = preco
xtres = preco*1.20
print('''Metodo de pagamento
[1] - Á vista dinheiro/cheque: 10% de desconto
[2] - Á vista no cartão: 5% de desconto
[3] - Em até 2x no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros''')
opcao = int(input('Opção: '))
if opcao == 1:
    print('Você deverá pagar R${:.2f}'.format(avista))
elif opcao == 2:
    print('Você deverá pagar R${:.2f}'.format(cartao))
elif opcao == 3:
    print('Você deverá pagar R${:.2f}'.format(xdois))
elif opcao == 4:
    print('Você deverá pagar R${:.2f}'.format(xtres))
else:
    print('Está opção não existe. Tente Novamente')