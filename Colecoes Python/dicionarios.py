"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}

print(type({}))

OBS: Sobre dicionários
	- Chave e valor são separados por dois pontos 'chave:valor';
	- Tanto chave quanto valor podem serde qualquer tipo de dado;
	- Podemos misturar tipos de dados;


# Criação de dicionarios

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))


# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['ru'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))


# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError
pais = paises.get('ru')

if pais:
	print(f'Encontrei o país {pais}')
else:
	print('Não encontrei o país')


# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('ru', 'não')

print(f'O país {pais} foi encontrado')
"""

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}



