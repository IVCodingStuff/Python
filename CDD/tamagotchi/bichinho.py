from biblioteca import *
idade = 1
peso = 2.5
continuar = True
print('=== TAMAGOTCHI ===')
nome = input('Qual o nome do seu novo pet? ')
print('Que belo nome!')
bichinho = Tamagotchi(nome, peso, idade)

while continuar:
        print('\n1.Comer\n2.Parar de comer\n3.Dormir\n4.Acordar\n5.Falar\n6.Parar de falar\n7.Sair')
        opcao = input('\nO que {} vai fazer? '.format(nome))
        if opcao in '1234567':
            if opcao == '1':
                bichinho.comer()

            if opcao == '2':
                print('comeu')
                bichinho.comeu()

            if opcao == '3':
                bichinho.dormir()

            if opcao == '4':
                bichinho.acordou()
                
            if opcao == '5':
                bichinho.falar()

            if opcao == '6':
                bichinho.falou()

            if opcao == '7':
                continuar = bichinho.parar(continuar)
        else:
            print('Opção inválida.')
            opcao = input('\nO que {} vai fazer? '.format(nome))
