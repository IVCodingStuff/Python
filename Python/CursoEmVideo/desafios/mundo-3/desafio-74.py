"""Gera números aleatórios e os coloca numa tupla"""
from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
maior = 0
for b in range(5):
    if numeros[b] > maior:
        maior = numeros[b]
menor = maior
for c in range(5):
   if numeros[c] < menor:
        menor = numeros[c]
print('Números sorteados:')
for d in range (5):
    print ('{}'.format(numeros[d]), end=' ')
print()
print('Menor valor sorteado: {}'. format(menor))
print('Maior valor sorteado: {}'. format(maior))

'''
   print ('{}'.format(max numeros))
   print ('{}'.format(min numeros))
'''