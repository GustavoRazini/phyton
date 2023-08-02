frase = str(input('DIGITE UMA FRASE QUALQUER:')).lower().strip()
l = str(input('ESCOLHA UMA LETRA PARA ANALISAR NA FRASE:')).lower().strip()

print ('A LETRA {} APARECE NA FRASE {}'.format(l, frase.count(l)))
print ('A LETRA {} APARECE PELA PRIMEIRA VEZ NA POSIÇÃO {}'.format(l, frase.find(l)+1))
print ('A LETRA {} APARECE PELA ÚLTIMA VEZ NA FRASE NA POSIÇÃO {}'.format(l, frase.rfind(l)+1))
