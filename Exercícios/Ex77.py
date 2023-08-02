
palvras = ('aprender', 'programar', 'linguagem',
           ' phyton', 'curso', 'gratis',
           'estudar', 'praticar', 'trabalhar',
           'mercado', 'programador', 'futuro')
for item in palvras:
    print(f'\nNa palavra {item.upper()} temos as vogais ',end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')