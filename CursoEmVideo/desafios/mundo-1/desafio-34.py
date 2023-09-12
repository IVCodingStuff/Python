sal = float(input('Insira seu salário e informarei seu aumento: '))

if sal > 1.250:
    sal = sal + (sal*10)/100
    print('Seu salário com aumento: {}'.format(sal))
else:
    sal = sal + (sal*15)/100
    print('Seu salário com aumento: {}'.format(sal)) 