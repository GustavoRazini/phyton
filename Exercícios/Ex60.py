n = int(input('Digite um valor: '))
c = n
f = 1
print('Cauculando {}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c> 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))