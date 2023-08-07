ano = int(input('Insira um ano e direi se ele é bissexto: '))

if ano % 4 == 0:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))
