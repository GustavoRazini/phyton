soma = n1 = c = 0
n1 = int(input('Digite um número inteiro, se quiser parar digite 999: '))
while n1 != 999:
    soma += n1
    c += 1
    n1 = int(input('Digite um número inteiro, se quiser parar digite 999: '))
print('Você digitou {} números inteiros, a soma entre eles é {}'.format(c,soma))