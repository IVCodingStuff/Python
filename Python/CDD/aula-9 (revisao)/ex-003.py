soma = float()
cont = 1
c = int(input('Quantos números deseja somar e ter a média? '))
while cont < c+1:
    num = float(input('Insira o {} número: '.format(cont)))
    soma += num
    cont += 1
media = soma/c
print('Soma: {}'.format(soma))
print('Média: {}'.format(media))