dis = int(input('Qual a distância percorrida durante a viagem? '))
if dis < 200:
    passagem = dis * 0.50
    print('O valor da passagem será de R${}.'.format(passagem))
else:
    passagem = dis * 0.45
    print('O valor da passagem será de R${}.'.format(passagem))
