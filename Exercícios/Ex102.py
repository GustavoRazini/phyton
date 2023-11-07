
"""
-> Calcula o fatorial do número digitado.
    :param n: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: Retorna o valor de n.
    """
if show == True:
    multiplicador = 1
    print('-'*20)
    for numero in range(num, 0, -1):
        multiplicador = multiplicador*numero
        print(numero, end='')
        print(' x ' if numero > 1 else ' = ', end='')
    return multiplicador
if show == False:
    multiplicador = 1
    print('-'*20)
    for numero in range(num, 0, -1):
        multiplicador = multiplicador*numero
    return multiplicador

print(fatorial(1, True))

