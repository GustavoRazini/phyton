valores = []
maior = menor = 0
for count in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {count}: ')))
    if count == 0:
        maior = menor = valores[count]
    else:
        if valores[count] > maior:
            maior = valores[count]
        if valores[count] < menor:
            menor = valores[count]

print('=-'*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ',end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
