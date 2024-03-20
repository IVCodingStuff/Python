n1 = int(input('Insira o 1ª numero: '))
n2 = int(input('Insira o 2ª numero: '))
n3 = int(input('Insira o 3ª numero: '))
maior = int()
if n1 > n2:
    maior = n1
else:
    maior = n2
if n3 > maior:
    maior = n3
print('O maior número inserido foi {}'.format(maior))