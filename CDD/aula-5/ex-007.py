soma= int()
c = int()
for c in range (1,5):
    num = int(input('Insira um número: '))
    soma += num
media = soma / c
print('A média aritmética dos números inseridos é: {}'.format(media))