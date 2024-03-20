n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
erro = 0
divisao = int()
while n2 == 0 and erro <= 4:
    print('Número inválido.')
    n2 = int(input('Insira o segundo número: '))
    erro += 1
    if erro == 5:
        print('Limite de tentativas alcançado')
        print('PROGRAMA FINALIZADO')
        break
else:
    divisao = n1/n2
    print(divisao)