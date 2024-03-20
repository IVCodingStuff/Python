anos = int(input('Qual a sua idade em anos? '))
meses = int(input('Quantos meses você viveu? '))
dias = int(input('Quantos dias você viveu? '))
tempovida = int()
tempovida += anos*365 + meses*30 + dias
print('Você viveu {} dias.'.format(tempovida))