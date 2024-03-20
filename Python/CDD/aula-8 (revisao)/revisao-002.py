n1 = int(input('Insira um número:'))
continuar = str()
while continuar in "Ss":
    while n1 == 0:
        print('Número inválido')
        n1 = int(input('Insira um número:'))
    if n1 > 0:
        print('Número positivo')
    else:
        print('Número negativo')
    continuar = input('Deseja continuar? [S/N] ')
