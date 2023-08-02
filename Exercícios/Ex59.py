from time import sleep
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
opc = 0
while opc != 5:
    print('=-='*10)
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    opc = int(input('Opção: '))
    if opc == 4:
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
    elif opc == 1:
        soma = num1 + num2
        print('A resultado de {} + {} é {}'.format(num1, num2, soma))
    elif opc == 2:
        multiplicacao = num1 * num2
        print('O resultado de {} X {} é {}'.format(num1, num2, multiplicacao))
    elif opc == 3:
        if num1 > num2:
            print('O primeiro valor digitado é maior do que segundo')
        if num2 > num1:
            print('O segundo valor digitado é maior do que o primeiro')
        else:
            print('Os dois valores são iguais')
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
    print('=-='*10)
    sleep(2)
print('Fim do programa')
