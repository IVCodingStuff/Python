tipocomb = input('Qual tipo de combustível quer abastecer? (E/G)')

    litroscomb = int(input('Com quantos litros deseja abastecer? '))
    if tipocomb == 'E' or 'e':
        preco = litroscomb * 4.90
        print ('Valor a ser pago: {}'.format(preco))
    if tipocomb == 'G' or 'g':
        preco = litroscomb * 5.80
        print('Valor a ser pago: {}'.format(preco))
else:
    print('Tipo de combustível inválido')

