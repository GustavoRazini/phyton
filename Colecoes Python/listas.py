"""
Listas
"""

lista1 = list(range(11))

num = int(input('Número: '))

if num in lista1:
	print(f'O número {num} está na lista')
else:
	print(f'O número {num} não está na lista')