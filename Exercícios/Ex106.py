def ajuda(com):
    help(com)


comando = ''
while True:
    comando = str(input('Função ouBiblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
