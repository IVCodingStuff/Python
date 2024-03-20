mostra = 0
while True:
    n1 = int(input('Insira um número:'))
    print('1. Mostrar o antecessor')
    print('2. Mostrar o sucessor')
    print('3. Finalizar o programa')
    mostra = (input('O que deseja fazer? '))
    if mostra == '1':
        ant = n1 - 1
        print('Antecessor: {}'.format(ant))
    elif mostra == '2':
        ant = n1 + 1
        print('Sucessor: {}'.format(ant))
    else:
        print('Programa Finalizado')
        break