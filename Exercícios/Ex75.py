n = int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o último número: '))
print(n)
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 foi digitado na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma vez')
print('Os valores pares digitados foram ',end='')
for num in n:
    if num % 2 == 0 and num != 0:
        print(f'{num} ',end='')
