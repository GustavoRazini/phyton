print('-=' * 15)
print('   10 TERMOS DE UM P.A')
print('-=' * 15)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Qual é a razão da P.A: '))
termo = primeiro
count = 1
while count <= 10:
    print('{}'.format(termo),end='')
    print(' -> 'if count <=9 else ' ',end='')
    termo+= razão
    count += 1
print('ACABOU')