soma = 0
count = 0
for c in range(1,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        count += 1
print('Você informou {} números pares e a soma foi {}'.format(count,soma))