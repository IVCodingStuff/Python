lista = [1,2,2,3,4,4,5,3,6,7,6,8]
nova_lista = []
for i in range (len(lista)):
    if lista[i] not in nova_lista:
        nova_lista.append(lista[i])
print(nova_lista)