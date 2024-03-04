info = [[], []]
pesados = []
leves = []
nome = a = p = 0
while True:
    info[0].append(str(input('Nome:')))
    info[1].append(int(input('Peso:')))
    print(info)
    print(a)
    if a == 1:
        print(info[1][1])
    if info[1][a] > pesados[0]:
        del pesados
        pesados.append(info[1][a])
    elif info[0][a] > pesados[0][0]:
        while pesados != 0:
            del (pesados[p])
            p+1

    if info[1][a] == pesos[1][0]:
        pesos[1][0].append(info[1][a])
    if info[1][a] == pesos[0][0]:
        pesos[1][0].append(info[0][a])

    elif info[1][a] < pesos[1][0]:
        del (pesos[1][0])
    resposta = (str(input('Deseja continuar? [S/N]')))
    if resposta in "Nn":
        break
    a += 1
print(info)
print(pesos)
print('Ao todo vocês cadastrou {} pessoas\nO maior peso foi {} Kg de {}\n O menor peso foi de Kg {} de {}'.format(a+1, pesos[0], pesos[1]))
