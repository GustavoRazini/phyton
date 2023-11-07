def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fes {gol} gol(s) no campenato.')


n = str(input('Nome do jogador: '))
g = int(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
