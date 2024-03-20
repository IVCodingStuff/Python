# Quantos números foram digitados, a lista de forma decrescente, se 5 está presente
lista = []
quantNum = 0
a = 0
while True:
    lista.append(int(input('Insira um valor:'))
                 )
    quantNum += 1
    resposta = input('Deseja continuar? [S/N]')
    if resposta in "Nn":
        break
print('Foram digitados {} números.'.format(quantNum))
print(lista)
lista.sort(reverse=True)
print('Os valores digitados foram {}'.format(lista))
if 5 in lista:
    print('O número 5 foi digitado.')
else:
    print('O número 5 não foi digitado.')
