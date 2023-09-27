senha = input('Insira a senha:')

print('PAYTHON')
print('Valor da compra: 100,00')
tentativaSenha = input('Senha:')
tentativas = 3
while tentativaSenha != senha:
    tentativas -= 1
    print('Senha Incorreta. Você tem mais {} tentativa(s).'.format(tentativas))
    tentativaSenha = input('Senha:')
    if tentativas == 1:
        print('Limite de tentativas alcançado. Cartão bloqueado.')
        print('PROGRAMA FINALIZADO')
        break
else:
    print('Compra autorizada.')