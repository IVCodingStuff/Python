'''#tuplas são imutáveis, pode ser escrita sem parênteses
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

for c in lanche:
    print('Vou comer {}.'.format(c))

for pos, c in enumerate(lanche):
    print('Vou comer {} na posição {}.'.format(c,pos))

for cont in range (0, len(lanche)):
    print(lanche[cont])

print (sorted(lanche))'''

a = (1,2,3,3)
b = (5,6,6,7)
c = a + b
print (c)
print (len(c))
print (c.index(5))
print (c.index(6,4)) 
""" O segundo número indica de onde começa a contar"""
del (c)
c = ('Mudou')
print(c)