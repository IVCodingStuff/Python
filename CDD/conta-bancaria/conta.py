from biblioteca import *
continuar = True
saldo = 0
status = False
conta = Conta(saldo, status)
print('===============')
print ('   BANCO CDD')
print('===============')
while continuar:
    
    if saldo > 0:
        print('\n1.Depositar\n2.Sacar\n3.Verificar o saldo\n4.Ativar conta\n5.Desativar conta\n6.Sair do sistema')
        opcao = int(input('\nO que deseja fazer? '))

        if opcao == 1:
            saldo = conta.depositar()

        if opcao == 2:
            conta.sacar()

        if opcao == 3:
            conta.verificar_saldo()

        if opcao == 4:
            status = conta.ativar()
            
        if opcao == 5:
            conta.desativar()

        if opcao == 6:
            continuar = conta.parar(continuar)

    else:
        print('\n1.Depositar\n2.Sacar\n3.Verificar o saldo\n4.Ativar conta\n5.Desativar conta\n6. Ativar limite\n7.Sair do sistema')
        opcao = int(input('\nO que deseja fazer? '))

        if opcao == 1:
            saldo = conta.depositar()

        if opcao == 2:
            conta.sacar()

        if opcao == 3:
            conta.verificar_saldo()

        if opcao == 4:
            status = conta.ativar()
            
        if opcao == 5:
            conta.desativar()

        if opcao == 6:
            conta.ativar_limite()

        if opcao == 7:
            continuar = conta.parar(continuar)