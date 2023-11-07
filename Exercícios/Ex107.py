from Exercícios.utidadescev import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Aumentando 10% de R${preco } temos R${moeda.aumentar(preco, 10)}')
