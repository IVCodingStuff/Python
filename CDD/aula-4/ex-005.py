soma = int()
for c in range (1, 11, 1):
    num = int(input('Insira um número: '))
    soma += num
media = soma/c
print('A soma dos números inseridos é: {}'.format(soma))
print ('A média desses números é: {:.2f}'.format(media))