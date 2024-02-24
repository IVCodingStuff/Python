#Lista crescente independente da ordem de inserção
lista = []
for a in range (5):
    num = int(input('Insira um valor: '))
    lista.append(num)
    for b in range (len(lista)):
        while lista[a] < lista[b]:
            lista.append(lista[b])
            del lista[b] 
print('Os números inseridos foram: {}'.format(lista))
