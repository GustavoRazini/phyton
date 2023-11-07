info = dict()
gols = list()
info['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {info["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
info['gols'] = gols[:]
info['total'] = sum(gols)
print('-='*30)
print(info)
print('-='*30)
for keys, value in info.items():
    print(f'O campo {keys} tem o valor {value}')
print('-='*30)
print(f'O Jogador {info["nome"]} jogou {len(info["gols"])} partidas')
for indice, valor in enumerate(info['gols']):
    print(f'    => Na partida {indice}, fez {valor} gols')
print(f'Foi um total de {info["total"]} gols')
