vel = int(input('Qual a velocidade do carro? '))
multa = ((vel-80) * 7)
if vel > 80:
    print('Você foi multado por ultrapassar o limite de velocidade. A multa é de R${}. Dirija com mais responsabilidade!'.format(multa))
else:
    print('Você não ultrapassou o limite e, por isso, não foi multado!')