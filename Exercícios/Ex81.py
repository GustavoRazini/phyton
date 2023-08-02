num = []
resp = ''
while resp != 'N':
    resp = ''
    n = int(input('Digite um valor: '))
    num.append(n)
    while resp != 'S' and resp != 'N':
        resp = str(input('Você quer continar? [S/N] ')).strip().upper()[0]
print('=-'*30)
print(f'Foram digitados {len(num)} valores')
num.sort(reverse=True)
print(f'A lista ordenada de forma decrecente {num}')
if 5 in num:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')