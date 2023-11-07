print('CONTROLE DE TERRENO')
def area(larg, comp):
    area = larg*comp
    print(f'A área de um terreno {largura}X{comprimento} é de {area}m².')

def mostralinha():
    print('-------------------')
mostralinha()
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)


