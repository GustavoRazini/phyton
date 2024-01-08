"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna data e hora corrente

print(datetime.datetime.now())  # 2023-12-13 17:00:04.604831  BR 13/12/2023

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horáriio para 16 horas, 0 minuto, 0 segundo, 0 microsegundo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do usuário e convertendo para data
print(type(evento))

print(type('31/12/2018'))

print(evento)

nascimento = input('Informe sua data de nacimento (dd/mm/yyyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))



"""

import datetime

evento = datetime.datetime(2019, 1, 1, 0)

# Acesso individual dos elementos de data e hora

print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minuto
print(evento.second)  # segundo
print(evento.microsecond)  # milisegundo

print(dir(datetime))