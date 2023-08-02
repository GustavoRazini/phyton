n = int(input('Digite um número inteiro: '))
print('''Escolha uma base de conversão:
(1) - Binário
(2) - Octal 
(3) - Hexadecimal''')
op = int(input('Digite sua opcão: '))
if op == 1:
    print('{} convertido para BINÁRIO é {}'.format(n,bin(n)))
elif op == 2:
    print('{} convertido para OCTAL é {}'.format(n,oct(n)))
elif op == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(n,hex(n)))
else:
    print('Opção inexistente, tente novamente')