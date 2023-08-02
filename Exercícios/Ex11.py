larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg*alt
litros = area/2
print('A área da parede é de {:.2f}m²\nSerá necessário {:.2f}L de tinta para pitar a parede. '.format(area,litros))