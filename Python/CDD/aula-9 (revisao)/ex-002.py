resp = str()
while resp in 'Ss':
    base = float(input('Base:'))
    while base == 0:
        print('Valor inválido.')
        base = float(input('Base:'))
    altura = float(input('Altura:'))
    while altura == 0:
        print('Valor inválido.')
        altura = float(input('Altura:'))
    area = (base*altura)/2
    print('Área:{}'.format(area))
    resp = input('Deseja fazer um novo calcúlo? [S/N] ')
print('Programa finalizado')