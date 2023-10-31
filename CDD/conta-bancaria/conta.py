from biblioteca import *
print ('BANCO CDD')
continuar = True
conta = Conta(500.0, True)

while continuar:
    print('1.Depositar\n2.Sacar\n3.Verificar o saldo\n4.Ativar conta\n5.Desativar conta\n6. Sair do sistema')
    opcao = int(input('O que deseja fazer? '))

    if opcao == 1:
        deposito = float(input('Quando quer depositar? '))
        conta.depositar(deposito)

    if opcao == 2:
        saque = float(input('Quanto quer sacar? '))
        conta.sacar(saque)

    if opcao == 3:
        conta.verificar_saldo()

    if opcao == 4:
        conta.ativar()

    if opcao == 5:
        conta.desativar()

    if opcao == 6:
        continuar = conta.parar(continuar)