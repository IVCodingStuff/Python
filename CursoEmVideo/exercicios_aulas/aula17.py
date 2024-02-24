#Lista são mutáveis
sanduiche = ['pão', 'carne', 'tomate', 'queijo', 'alface', 'ketchup']
sanduiche.append('mostarda')
#Adiciona no fim da lista

sanduiche.insert(0, 'bacon')
#Adiciona num local especifico
del sanduiche[2]

sanduiche.pop(5)
#Usado para deletar o ultimo elemento, mas pode ser especificado

if 'tomate' in sanduiche:
    sanduiche.remove('tomate')

valores = list(range(4, 11))
valores.sort
#organiza do menor pro maior

valores.sort(reverse=True)
#organiza do maior pro menor

print(sanduiche)
