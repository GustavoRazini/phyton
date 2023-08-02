tabelabrasileirao = ('Botafogo', 'Flamengo', 'Grêmio', 'São Paulo', 'Fluminense',
'Palmeiras', 'Bragantino', 'Athletico-PR', 'Fortaleza', 'Cruzeiro',
'Internacional', 'Atlético-MG', 'Cuiabá', 'Santos', 'Corinthians',
'Bahia', 'Goiás', 'Coritiba', 'Vasco', 'América-MG')
print(f'Lista de times Brasileirão: {tabelabrasileirao}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=')
print('Os primeiros 5 colocados do Brasileirão são: ',end='')
for c in range(0,5):
    print(f'{c+1}-{tabelabrasileirao[c]}', '-> 'if c <4 else '',end='')
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Os times que estão em zona de rebaixamento são: ',end='')
for d in range(16,len(tabelabrasileirao)):
    print(f'{d+1}-{tabelabrasileirao[d]}','-> 'if d < 19 else '',end='')
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Tabela do Brasileirão em ordem alfabética: {sorted(tabelabrasileirao)}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=')
print('Posição Flamengo tabela Brasileirão:')
print(tabelabrasileirao.count('Flamengo')+1,'ºLugar')