import math
angulo = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ÂNGULO {.:2f} tem o SENO {.:2f}, COSSENO {.:2f} e a TANGENTE {.:2f}'.format(angulo,seno,cosseno,tangente))
