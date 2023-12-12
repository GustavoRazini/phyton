"""
POO - Polimorfismo

Pooli -> Muitas
Morfis -> Formas

Quando agente reimplemnta um método presente na classe pai em classes filhas
estamos realizando uma sobrescrita de método (Overriding).

O overrinding é a essência do polimorfismo./
"""


class Animal(object):
	def __init__(self, nome):
		self.nome = nome

	def falar(self):
		raise NotImplementedError('Aclasse filha precisa implementar esse método')

	def comer(self):
		print(f'{self.nome} está comedo...')


class Cachorro(Animal):
	def __init__(self, nome):
		super().__init__(nome)

	def falar(self):
		print(f'{self.nome} fala au au')


class Gato(Animal):

	def __init__(self, nome):
		super().__init__(nome)

	def falar(self):
		print(f'{self.nome} fala miau!')


class Rato(Animal):

	def __init__(self, nome):
		super().__init__(nome)

	def falar(self):
		print(f'{self.nome} fala algo...')


# Testes

felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mikey = Rato('Mickey')
mikey.comer()
mikey.falar()
