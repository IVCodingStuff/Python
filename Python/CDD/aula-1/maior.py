num1 = int(input('Insira o 1º número: '))
num2 = int(input('Insira o 2º número: '))
num3 = int(input('Insira o 3º número: '))

if num1 > num2:
    maior = num1
else:
    maior = num2
if num3 > maior:
    maior = num3

print('O maior número inserido é: {}'.format(maior))
