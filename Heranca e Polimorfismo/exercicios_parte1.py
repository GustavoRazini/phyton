"""class Pessoa:
	def __init__(self, nome, endereco, telefone):
		self.nome = nome
		self.endereco = endereco
		self.telefone = telefone

	def imprimir(self):
		print(f'Nome: {self.nome}')
		print(f'Endereço: {self.endereco}')
		print(f'Telefone: {self.telefone}')


# Criando instância da classe Pessoa
pessoa1 = Pessoa(nome="Gustavo", endereco="Rua A, 123", telefone="123456789")
# Chamando o método imprimir para exibir os atributos
pessoa1.imprimir()



class Quadrado:

	def __init__(self, lado):
		self.lado = lado

	def cacular_area(self):
		return self.lado * self.lado

	def cacular_perimetro(self):
		return 4 * self.lado

	def imprimir(self):
		print(f'Lado: {self.lado}')
		print(f'Área: {self.cacular_area()}')
		print(f'Perímetro: {self.cacular_perimetro()}')


q1 = Quadrado(5)

q1.imprimir()




class Retangulo:
	def __init__(self, comprimento, largura):
		self.comprimento = comprimento
		self.largura = largura

	def calcular_area(self):
		return self.largura * self.comprimento

	def calcular_perimetro(self):
		return (2 * self.largura) + (2 * self.comprimento)

	def imprimir(self):
		print(f'Largura: {self.largura}')
		print(f'Comprimento: {self.comprimento}')
		print(f'Área: {self.calcular_area()}')
		print(f'Perímetro: {self.calcular_perimetro()}')


r1 = Retangulo(7, 15)

r1.imprimir()


from math import pi


class Circulo:

	def __init__(self, raio):
		self.raio = raio

	def calcular_area(self):
		return (pi * self.raio * self.raio)

	def calcular_perimetro(self):
		return (2 * pi * self.raio)

	def imprimir(self):
		print(f'Raio: {self.raio}')
		print(f'Área: {self.calcular_area():.2f}')
		print(f'Perímetro: {self.calcular_perimetro():.2f}')


c1 = Circulo(5)

c1.imprimir()




class Moto:
	marchas = {
		0: 'marcha neutra',
		1: 'primeira marcha',
		2: 'segunda marcha',
		3: 'terceira marcha',
		4: 'quarta marcha',
		5: 'quinta marcha',
		6: 'sexta marcha'
	}

	def __init__(self, marca, modelo, cor, marcha):
		self.marca = marca
		self.modelo = modelo
		self.cor = cor
		self.marcha = self.marchas.get(marcha, 'Essa marcha não existe')
		self.ligada = True

	def imprimir(self):
		if self.ligada == True:
			print(
				f'A moto da marca {self.marca} do modelo {self.modelo} da cor {self.cor} e se encontra na {self.marcha} e está ligada')
		else:
			print(
				f'A moto da marca {self.marca} do modelo {self.modelo} da cor {self.cor} e se encontra na {self.marcha} e está desligada')

	def mudar_marcha(self, direcao):
		self.marcha = self.marchas.get(self.marchas.get(self.marcha, 0) + direcao, 'A marcha atingiu seu limite')

	def ligada_desligada(self):
		if self.ligada is True:
			self.ligada = False
		else:
			self.ligada = True


moto1 = Moto('Honda', 'Hornet', 'preta', 0)
moto1.imprimir()
moto1.mudar_marcha(1)
moto1.ligada_desligada()
moto1.imprimir()




class Eletrodomesticos:
	def __init__(self):
		self.ligada = True

	def imprimir(self):
		if self.ligada == True:
			print('O eletrodomestico está ligado')
		else:
			print('O eletrodomestico está desligado')

	def ligada_desligada(self):
		if self.ligada is True:
			self.ligada = False
		else:
			self.ligada = True

# Create an instance of the Eletrodomesticos class
appliance = Eletrodomesticos()

# Print the initial state
appliance.imprimir()  # Output: O eletrodomestico está ligado

# Toggle the state
appliance.ligada_desligada()

# Print the updated state
appliance.imprimir()  # Output: O eletrodomestico está desligado




class Televisor:

    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
        self.ligada = True

    def imprimir(self):
        print(f'Canal: {self.canal}')
        print(f'Volume: {self.volume}')
        print(f'Ligada: {self.ligada}')

    def ligada_desligada(self):
        self.ligada = not self.ligada

    def numero_canais(self):
        if self.canal > 100:
            self.canal = 100
            print('O maior canal é o 100')
        elif self.canal < 1:  # Alteração aqui para garantir que o canal não seja menor que 1
            self.canal = 1
            print('O menor canal é o 1')

    def volume_total(self):
        if self.volume > 100:
            self.volume = 100
            print('O maior volume é o 100')
        elif self.volume < 0:  # Alteração aqui para garantir que o volume não seja menor que 0
            self.volume = 0
            print('O menor volume é o 0')

    def canal_acima(self):
        if self.canal < 100:
            self.canal += 1
        else:
            print('O maior canal é 100')

    def canal_abaixo(self):
        if self.canal > 1:
            self.canal -= 1
        else:
            print('O menor canal é 1')

    def volume_acima(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print('O maior volume é 100')

    def volume_abaixo(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print('O menor volume é 0')


# Create an instance of the Televisor class
tv = Televisor(canal=5, volume=50)

# Print the initial state
tv.imprimir()

# Toggle the power state
tv.ligada_desligada()
tv.imprimir()

# Change the channel and volume
tv.canal_acima()
tv.volume_acima()
tv.imprimir()

# Try to set an invalid channel and volume
tv.canal = 105
tv.volume = -10
tv.numero_canais()
tv.volume_total()
tv.imprimir()

# Change the channel and volume below the minimum
tv.canal_abaixo()
tv.volume_abaixo()
tv.imprimir()




class Microondas:

	def __init__(self):
		self.ligada = True
		self.porta = True

	def imprimir(self):
		if self.porta == True:
			print(f'O micro ondas está ligado? {self.ligada}')
			print(f'e a porta está fechada')
		else:
			print(f'O micro ondas está ligado? {self.ligada}')
			print(f'e a porta está aberta')

	def ligada_desligada(self):
		self.ligada = not self.ligada

	def abrir_porta(self):
		if self.porta == True:
			self.porta = False
		else:
			self.porta = True

"""
