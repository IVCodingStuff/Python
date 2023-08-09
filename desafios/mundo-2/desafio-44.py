preco = float(input('Valor do produto: '))
print ('Informe a forma de pagamento:')
print ('[1] - Dinheiro/Cheque')
print ('[2] - Cartão de débito')
print ('[3] - Cartão de crédito (Até 2x sem juros)')
opcao = int(input('Opção de pagamento: '))

if opcao == 1:
    preco = preco - ((preco*10)/100)
    print('Total a ser pago: {}'.format(preco))
elif opcao == 2:
    preco = preco - ((preco*5)/100)
    print('Total a ser pago: {}'.format(preco))
elif opcao == 3:
    parcelas = int(input('Em quantas vezes quer dividir? '))
    if (parcelas == 1) or (parcelas == 2):
        print('Total a ser pago: {}'.format(preco))
    elif parcelas >= 3:
        preco = preco + ((preco*20)/100)
        print('Total a ser pago: {}'.format(preco))


