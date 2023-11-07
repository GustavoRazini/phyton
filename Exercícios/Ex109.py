from Exercícios.utidadescev import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(preco)} é R${moeda.metade(preco, True)}')
print(f'O dobro de R${moeda.moeda(preco)} é R${moeda.dobro(preco, True)}')
print(f'Aumentando 10% de R${moeda.moeda(preco)} temos R${moeda.aumentar(preco, 10, True)}')
