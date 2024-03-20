s = float()
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print('[1] somar')
print('[2] multiplicar')
print('[3] maior')
print('[4] novos números')
print('[5] sair do programa')
opcao = int(input('O que deseja fazer? '))
while opcao != 5:
    print()
    if opcao == 1:
        print()
        s = n1 + n2
        print ('{} + {} = {}'.format(n1,n2,s))
    if opcao == 2:
        print()
        m = n1 * n2
        print ('{} * {} = {}'.format(n1,n2,m))
    if opcao == 3:
        print()
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print ('O maior número é {}.'.format(maior))
    if opcao == 4:
        print()      
        n1 = float(input('Digite um novo número:'))
        n2 = float(input('Digite outro número:'))
    print()
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    opcao = int(input('O que deseja fazer? '))
print()  
print('Fim do programa')           
