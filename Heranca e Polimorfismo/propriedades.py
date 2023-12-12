"""
POO - Propriedades - Properties

Em liguagens de programação como Java, ao declarmos atributos privados nas classes,
costumamos a criar métodos públicos para manipulação desses atributos. Esses métodos
são conhecidos por getters e setters, onde os getters retornam o valor do atributo
e os setters alteram o valor do mesmo.

Olá meu nome não é Igor


"""


class Conta:
	contador = 0

	def __init__(self, titular, saldo, limite):
		self.numero = Conta.contador + 1
		self.titular = titular
		self.saldo = saldo
		self.limite = limite
		Conta.contador += 1

	def extrato(self):
		return f'Saldo de {self.saldo} do cliente {self.titular}'

	def depositar(self, valor):
		self.saldo += valor

	def sacar(self, valor):
		self.saldo -= valor

	def transferir(self, valor, destino):
		self.saldo -= valor
		destino.saldo += valor


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {soma}')
