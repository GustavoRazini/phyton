s1 = float(input('Medida do segmento 1: '))
s2 = float(input('Medida do segmento 2: '))
s3 = float(input('Medida do segmento 3: '))

maior = max(s1, s2, s3)
soma = (s1 + s2 + s3) - maior

if soma <= maior:
    print('Não é possível formar um triângulo.')
elif s1 == s2 and s2 == s3:
    print('Triângulo EQUILÁTERO')
elif s1 != s2 and s1 != s3 and s2 != s3:
    print('Triângulo ESCALENO')
else:
    print('Triângulo ISÓCELES')
