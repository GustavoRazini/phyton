"""
POO - Objetos

Objetos -> São intâncias da classe. Ou  sjea, após o mapeamento do objeto do mundo real para sua representação
computacional, devemos poder criar quantos objetos forem necessáros. Podemos pensar nos objetos/instâncias de uma classe
como variáveis do tipo definido na classe.

# Instâcias/Objetos
lamp1 = Lampada('branca', 110, 60)

lamp1.ligar_desligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

lamp1.ligar_desligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 20000)

user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456'),
"""


class Lampada:

	def __init__(self, cor, voltagem, luminosidade):
		self.__cor = cor
		self.__voltagem = voltagem
		self.__luminosidade = luminosidade
		self.__ligada = False

	def checa_lampada(self):
		return self.__ligada

	def ligar_desligar(self):
		if self.__ligada:
			self.__ligada = False
		else:
			self.__ligada = True

class Cliente:
	def __init__(self, nome, cpf):
		self.__nome = nome
		self.__cpf = cpf
	def diz (self):
		print(f'O cliente {self.__nome} diz oi')

class ContaCorrente:
	contador = 4999

	def __init__(self, limite, saldo, cliente):
		self.__numero = ContaCorrente.contador + 1
		self.__limite = limite
		self.__saldo = saldo
		self.__cliente = cliente
		ContaCorrente.contador = self.__numero

	def mostra_corrente(self):
		print(f'O cliente é {self.__cliente._Cliente__nome}')
class Usuario:
	def __init__(self, nome, sobrenome, email, senha):
		self.__nome = nome
		self.__sobrenome = sobrenome
		self.__email = email
		self.__senha = senha


cli1 = Cliente('Angelina Jolie', '123.456.789-99')

cc = ContaCorrente(5000, 10000, cli1)

cc.mostra_corrente()

cc._ContaCorrente__cliente.diz()