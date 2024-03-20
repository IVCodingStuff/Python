confirmar = str()
while confirmar in 'Ss':
    n1 = float(input('Insira um número: '))
    n2 = float(input('Insira outro número: '))
    media = (n1+n2)/2
    print(media)
    if media >= 7:
        print('APROVADO')
    elif media >= 4:
        print('RECUPERAÇÃO')
    else:
        print('REPROVADO')
    confirmar = input('Quer fazer mais um cálculo?[S/N] ')
