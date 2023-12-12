"""
class Usuario:
	def __init__(self, nome, idade, altura):
		self.__nome = nome
		self.__idade = idade
		self.__altura = altura

	# Getter para o nome
	@property
	def nome(self):
		return self.__nome

	# Setter para o nome
	@nome.setter
	def nome(self, novo_nome):
		self.__nome = novo_nome

	# Getter para a idade
	@property
	def idade(self):
		return self.__idade

	# Setter para a idade
	@idade.setter
	def idade(self, nova_idade):
		self.__idade = nova_idade

	# Getter para a altura
	@property
	def altura(self):
		return self.__altura

	# Setter para a altura
	@altura.setter
	def nome(self, nova_altura):
		self.__altura = nova_altura

	def imprimir_detalhes(self):
		print(f'Nome: {self.__nome}; Idade: {self.__idade}; Altura: {self.__altura}')


user1 = Usuario(nome='Gustavo', idade=15, altura=1.85)


Usuario.imprimir_detalhes(user1)

# Criando uma instância da classe Agenda
agenda = Agenda()

# Adicionando uma pessoa à agenda
agenda.armazena_pessoa('Gustavo', 15, 1.85)

# Imprimindo a lista de pessoas
print(agenda.pessoas)

# Removendo a pessoa da agenda
agenda.remove_pessoa('Gustavo')

# Imprimindo a lista de pessoas (deve estar vazia neste ponto)
print(agenda.pessoas)

# Criando uma instância da classe Agenda
agenda = Agenda()

# Adicionando algumas pessoas à agenda
agenda.armazena_pessoa('Gustavo', 15, 1.85)
agenda.armazena_pessoa('Alice', 25, 1.70)
agenda.armazena_pessoa('Jonas', 30, 1.80)

# Imprimindo a lista de pessoas
print(agenda.pessoas)

# Buscando pessoas na agenda
agenda.busca_pessoa('Gustavo')
agenda.busca_pessoa('Alice')
agenda.busca_pessoa('Maria')  # Um exemplo de pessoa que não está na agenda

"""


class Agenda:
	def __init__(self):
		self.pessoas = []

	def armazena_pessoa(self, nome, idade, altura):
		if len(self.pessoas) < 10 and nome not in [pessoa['Nome'] for pessoa in self.pessoas]:
			pessoa = {'Nome': nome, 'Idade': idade, 'Altura': altura}
			self.pessoas.append(pessoa)
			print('Nome adicionado...')
			return
		else:
			print('Agenda cheia ou nome já existente...')
			return

	def remove_pessoa(self, nome):
		for pessoa in self.pessoas:
			if pessoa['Nome'] == nome:
				self.pessoas.remove(pessoa)
				print('Pessoa removida com sucesso...')
				return
		print('Nome inexistente...')
		return

	def busca_pessoa(self, nome):
		for contador, pessoa in enumerate(self.pessoas, start=1):
			if pessoa['Nome'] == nome:
				print(f'{nome} está na posição {contador} da agenda.')
				return
		print(f'{nome} não está na agenda.')

	def imprime_agenda(self):
		print(self.pessoas)

	def imprime_pessoa(self, index):
		if 1 <= index <= len(self.pessoas):
			print(self.pessoas[index - 1])
		else:
			print('Índice inválido.')

	def __str__(self):
		return str(self.pessoas)


# Criando uma instância da classe Agenda
agenda = Agenda()

# Adicionando algumas pessoas à agenda
agenda.armazena_pessoa('Gustavo', 15, 1.85)
agenda.armazena_pessoa('Alice', 25, 1.70)
agenda.armazena_pessoa('Jonas', 30, 1.80)

# Imprimindo a lista de pessoas usando o método imprime_agenda
agenda.imprime_agenda()

# Buscando pessoas na agenda
agenda.busca_pessoa('Gustavo')
agenda.busca_pessoa('Alice')
agenda.busca_pessoa('Maria')  # Um exemplo de pessoa que não está na agenda

# Imprimindo pessoa por índice
agenda.imprime_pessoa(2)

# Imprimindo a representação da agenda usando __str__
print(agenda)
