from biblioteca import *

while True:
    opcao = input(('1. Somar\n2. Subtrair\n3.Multiplicar \n4.Dividir\n5. Trocar os números\nS. Sair\nO que quer fazer?'))
    while opcao not in "12345Ss":
        print('Opção inválida>')
        opcao = input(
            ('1. Somar\n2. Subtrair\n3.Multiplicar \n4.Dividir\n5. Trocar os números\nS. Sair\nO que quer fazer?'))
        if opcao != 'sS':
            n1 = int(input('Primeiro número: '))
            n2 = int(input('Segundo número: '))

        if opcao == '1':
            soma(n1, n2)
        elif opcao == '2':
            sub(n1, n2)
        elif opcao == '3':
            multi(n1, n2)
        elif opcao == '4':
            divi(n1, n2)
        elif opcao == '5':
            print('Números atualizados com sucesso!')
            print('\n')
        elif opcao in 'Ss':
            print('Programa Finalizado')
            break
        else:

            print('===============')
            print('Valor inválido')
            print('===============')