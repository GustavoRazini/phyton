from time import sleep

print('#' * 12, ' SISTEMA ', '#' * 12)
sleep(1)
produto = {}
cliente = {}
produtos = []
clientes = []
while True:
	print("""
	1 - Cadastrar Cliente
	2 - Cadastrar Produto
	3 - Listar Produtos
	4 - Listar Clientes
	5 - Deletar Produto
	6 - Deletar Cliente
	7 - Atualizar Produtor
	8 - Atualizar Cliente
	
	0 - Sair """)
	resp = int(input('Resposta: '))
	if resp == 0:
		break
	elif resp == 1:
		cliente['cpf'] = str(input('Cpf cliente: '))
		cliente['nome'] = str(input('Nome do cliente: '))
		while True:
			try:
				cliente['idade'] = int(input('idade do cliente: '))
				break
			except ValueError:
				print('O valor deve ser inteiro')
		clientes.append(cliente)
	elif resp == 2:
		produto['nome'] = str(input('Nome do produto: '))
		while True:
			try:
				produto['valor'] = float(input('Valor do produto R$'))
				break
			except ValueError:
				print('O valor deve ser um valor númerico')
		produtos.append(produto)
	elif resp == 3:
		if produtos != []:
			for produto in produtos:
				print(produto)
	elif resp == 4:
		if clientes != []:
			for cliente in clientes:
				print(cliente)
	elif resp == 5:
		if produtos != []:
			tamanho_produto = len(produto)
			produtos.remove(produto[tamanho_produto])
	elif resp == 6:
		if clientes != []:
			tamanho_cliente = len(clientes)
			clientes.remove(cliente[tamanho_cliente])
	elif resp == 7:
		pass
	elif resp == 8:
		pass
sleep(2)
print('#' * 34)
