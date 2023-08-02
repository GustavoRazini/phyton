tot18 = toth = totM20 = 0
while True:
    print('-'*7,'CADASTRE UMA PESSOA','-'*7)
    idade = int(input('Idade: '))
    sexo = ' '
    if sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {tot18}
Ao todo temos {toth} homens cadastrados
E temos {totM20} mulheres com menos de 20 anos''')



