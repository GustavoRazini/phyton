print('-=' * 15)
print('   10 TERMOS DE UM P.A')
print('-=' * 15)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Qual é a razão da P.A: '))
décimo = primeiro + 10 * razão
for c in range(primeiro, décimo, razão):
    print(c, end = ' → ')
print('ACABOU')