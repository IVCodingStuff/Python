time1 = input('Insira o nome do primeiro time: ')
time2 = input('Insira o nome do segundo time: ')
gols1 = input( 'Insira o número de gols de {}: '.format(time1))
gols2 = input( 'Insira o número de gols de {}: '.format(time2))

if gols1 > gols2:
    print('TIME VENCEDOR:{}'.format(time1))
elif gols1 < gols2:
    print('TIME VENCEDOR:{}'.format(time2))
else:
    print('EMPATE')