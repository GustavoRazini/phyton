matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maiorvalor = somacoluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
        if matriz[linha][2]:
            somacoluna += matriz[linha][2]
        if matriz[linha][coluna] == matriz[0][0]:
            maiorvalor = matriz[linha][coluna]
        else:
            if maiorvalor < matriz[linha][coluna]:
                maiorvalor = matriz[linha][coluna]
print()
print('=-'*30)
print(f'A soma entre todos os valores pares digitados é {somapar}')
print(f'A soma dos valolres da terceira coluna é {somacoluna}')
print(f'O maior valor é {maiorvalor}')

