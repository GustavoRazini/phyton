from datetime import datetime
count = 0
count1 = 0
atual = datetime.today().year
for c in range(1,8):
    pessoas = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual- pessoas
    print('Está pessoa tem {} anos de idade em {}'.format(idade,atual))
    if idade >= 21:
        count += 1
    else:
        count1 += 1
print('''Ao todo temos {} pessoas maiores de idade
e também {} pessoas menores de idade'''.format(count,count1))