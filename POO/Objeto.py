class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self._voltagem = voltagem
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


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__saldo = senha


lamp1 = Lampada('branca', 110, 60)

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

lamp1.ligar_desligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 20000)

nome = 'Angelina'
sobrenome = 'Jolie'
email = 'agelina@gmail.com'
senha = '123456'

user = Usuario(nome, sobrenome, email, senha)


print(type(42))
print(type(user))
print(type('gustavo'))

class Ex:
    def Helper(self, texto, senha):
        self.__texto = texto
        self.__senha = senha