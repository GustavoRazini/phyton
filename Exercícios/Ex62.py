print('-=' * 15)
print('   10 TERMOS DE UM P.A')
print('-=' * 15)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Qual é a razão da P.A: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print('{}'.format(termo),end='')
        print(' -> 'if count <=total else ' ',end='')
        termo+= razão
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progreção finalizada com {} termos mostrados.'.format(total))
