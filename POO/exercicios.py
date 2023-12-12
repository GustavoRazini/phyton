"""
class Usuario:
	def __init__(self, nome, idade, altura):
		self.__nome = nome
		self.__idade = idade
		self.__altura = altura

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, novo_nome):
		self.__nome = novo_nome

	@property
	def idade(self):
		return self.__idade

	@idade.setter
	def nome(self, nova_idade):
		self.__idade = nova_idade

	@property
	def altura(self):
		return self.__altura

	@altura.setter
	def nome(self, nova_altura):
		self.__altura = nova_altura

	def imprimir_detalhes(self):
		print(f'Nome: {self.__nome}; Idade: {self.__idade}; Altura: {self.__altura}')
-----------------------------------------------------------------------------------------
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
-----------------------------------------------------------------------------------------

class Elevador:

	def __init__(self, capacidade, total_andares):
		self.capacidade = capacidade
		self.total_andares = total_andares
		self.andar_atual = 0
		self.quantidade_pessoas = 0

	def entrar(self):
		if self.capacidade > self.quantidade_pessoas:
			self.quantidade_pessoas += 1
		else:
			print('Já tem pessoas de mais no elevador...')

	def sai(self):
		if self.quantidade_pessoas != 0:
			self.quantidade_pessoas -= 1

	def sobe(self):
		if self.andar_atual != self.total_andares:
			self.andar_atual += 1

	def desce(self):
		if self.andar_atual != 0:
			self.andar_atual -= 1

	def mostra_dados(self):
		print(f"Capacidade: {self.capacidade}")
		print(f"Total de Andares: {self.total_andares}")
		print(f"Andar Atual: {self.andar_atual}")
		print(f"Total de Pessoas: {self.quantidade_pessoas}")


elevador = Elevador(10, 5)

elevador.mostra_dados()
print()
elevador.entrar()
elevador.entrar()
print()
elevador.mostra_dados()
print()
elevador.sai()
print()
elevador.mostra_dados()
print()
elevador.sobe()
elevador.sobe()
elevador.sobe()
print()
elevador.mostra_dados()
print()
elevador.desce()
elevador.desce()
elevador.desce()
elevador.desce()
elevador.desce()
elevador.desce()
elevador.desce()
elevador.desce()
print()
elevador.mostra_dados()
-----------------------------------------------------------------------------------------

"""


class Televisao:
	def __init__(self):
		self.ligada = False
		self.canal = 1
		self.volume = 50

	def ligar_desligar(self):
		self.ligada = not self.ligada

		if self.ligada:
			print('A televisão está ligada')
		else:
			print('A televisão está deligada')

	def trocar_canal(self, canal_novo):
		if self.ligada:
			self.canal = canal_novo
			print(f'Canal alterado para {canal_novo}')

	def aumentar_volume(self):
		if self.volume < 100 and self.ligada:
			self.volume += 1
			print(f'O volume foi aumentado para {self.volume}')
		elif self.ligada:
			print('Volume máximo')
		else:
			print('A televisão está desligada')

	def diminuir_volume(self):
		if self.volume > 0 and self.ligada:
			self.volume -= 1
			print(f'O volume foi diminuido para {self.volume}')
		elif self.ligada:
			print('Volume mínimo')
		else:
			print('A televisão está desligada')


class ControleRemoto:
	def __init__(self, televisao):
		self.televisao = televisao

	def ligar_desligar_tv(self):
		self.televisao.ligar_desligar()

	def trocar_canal_tv(self, canal_novo):
		self.televisao.trocar_canal(canal_novo)

	def aumentar_volume_tv(self):
		self.televisao.aumentar_volume()

	def diminuir_volume_tv(self):
		self.televisao.diminuir_volume()


# Teste

televisao_sala = Televisao()
controle_sala = ControleRemoto(televisao_sala)

controle_sala.ligar_desligar_tv()
controle_sala.trocar_canal_tv(5)
controle_sala.aumentar_volume_tv()
controle_sala.diminuir_volume_tv()
