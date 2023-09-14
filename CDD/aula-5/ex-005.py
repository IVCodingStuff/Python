negativo = int()
soma = int()
positivo = int()
for c in range(1,9,1):
    num = int(input('Insira um número:'))
    if num <0 :
        negativo += 1
        soma += num
    positivo = c - negativo
print('Foram inseridos {} números negativos.'.format(negativo))
print('A soma dos números negativos é: {}'.format(soma))
print('Foram inseridos {} números positivos.'.format(positivo))