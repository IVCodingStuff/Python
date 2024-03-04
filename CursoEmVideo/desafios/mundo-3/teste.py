info = [[], []]
pesados = [0]
leves = [0]
nomes = [['a'], ["a"]]
a = p = l = 0
while True:
    info[0].append(str(input('Nome:')))
    info[1].append(int(input('Peso:')))
    print(info)
    if info[1][a] > pesados[0]:
        p = 0
        while p < a+1 :
            del (pesados[p])
            del (nomes[0][p])
            p += 1
        pesados.append(info[1][a])
        nomes[0].append(info[0][a])
    elif info[1][a] == pesados[0]:
        pesados.append(info[1][a])
        nomes[0].append(info[0][a])

    if a == 0:
        leves[0] = (info[1][a])
    print('leves: {}'.format(leves[0]))

    if info[1][a] < leves[0]:
        l = 0
        print('valor de l: {}'.format(l))
        while l < a+1 :
            del (leves[l])
            del (nomes[0][l])
            l += 1
        leves.append(info[1][a])
        nomes[0].append(info[0][a])
    elif info[1][a] == leves[0]:
        leves.append(info[1][a])
        nomes[0].append(info[0][a])

    resposta = (str(input('Deseja continuar? [S/N] ')))
    if resposta in "Nn":
        break
    a += 1
print('Ao todo vocês cadastrou {} pessoas\nO maior peso foi {} Kg de {}\nO menor peso foi de Kg {} de {}'.format(
    a+1, pesados[0], nomes[0], leves, nomes[1]))
