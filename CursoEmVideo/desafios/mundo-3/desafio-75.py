"""Lê 4 valores, os coloca numa tupla e diz algumas informações sobre"""
numeros = (int(input('Insira um número:')), int(input('Insira um número:')), int(input('Insira um número:')), int(input('Insira um número:')))
nove = 0
tres = 0
pares = []
for b in range (4):
    if numeros[b] == 9:
        nove += 1
for c in range (4):
    if numeros[c] == 3:
        tres = c + 1
        break
for d in range (4):
    if numeros [d] % 2 == 0:
        pares.append(numeros[d])
        
print('O valor 9 apareceu {} vez(es)'.format(nove))
#print('O valor 9 apareceu {} vez(es)'.format(numeros.count(9)))
if 3 in numeros:
   print('Posição do valor 3: {}º'.format(numeros.index(3)+1))
else:
  print('O valor 3 não foi digitado.')
  
print('Números pares: {}'.format(pares))
