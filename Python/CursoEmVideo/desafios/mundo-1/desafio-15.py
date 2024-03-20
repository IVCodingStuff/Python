km = float(input('Qual a quantidade de Km percorrida? '))
dias = int(input('Quantos dias você ficou com o carro? '))
al = (dias*60) + (km*0.15)
print('O valor a ser pago é de R${}.'.format(al))