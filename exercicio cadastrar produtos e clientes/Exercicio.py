produto = {}
cliente = {}

continuar = 'S'

while True:
	if continuar in 'S':
		cliente['cpf'] = str(input('Cpf cliente: '))
		cliente['nome'] = str(input('Nome do cliente: '))
	while True:
		try:
			cliente['idade'] = int(input('idade do cliente: '))
			break
		except ValueError:
			print('O valor deve ser inteiro')
	produto['nome'] = str(input('Nome do produto: '))
	while True:
		try:
			produto['valor'] = float(input('Valor do produto R$'))
			break
		except ValueError:
			print('O valor deve ser um valor númerico')

	continuar = str(input('Quer continuar? S/N ')).upper()[0]
	if continuar == 'N':
		break
	while continuar != 'S':
		continuar = str(input('Quer continuar? S/N')).upper()[0]
