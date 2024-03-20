lista = []
pares = []
impares = []
a = 0
while True:
    lista.append((int(input('Insira um número: '))))
    a += 1
    resposta = (str(input('Quer continuar?[S/N] ')))
    if resposta in "Nn":
        break
for b in range(len(lista)):
    if (lista[b]) % 2 == 0:
        pares.append(lista[b])
    else:
        impares.append(lista[b])
lista.sort()
print('Números digitados: {}'.format(lista))
print('Números pares digitados: {}'.format(pares))
print('Números impares digitados: {}'.format(impares))
