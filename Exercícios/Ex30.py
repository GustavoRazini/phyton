
num = int(input('\033[1;35mMe diga um número qualquer: '))

if num % 2 == 0:
    print('O número {} é \033[4;36mPAR'.format(num))
else:
    print('O número {} é \033[4;36mÍMPAR'.format(num))