from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*25)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior =valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(9,2,8,6)
maior(92,22,52,16)
maior(42,24,5,1)