media = 0
maior = 0
num = [0]*30
pares =[0]*30
maiormedia = 0
e = 0
for c in range(30):
    num[c] = int(input('Insira o {}º número: '.format(c+1)))
    media += num[c]
for d in range(30):    
    if num[d] % 2 == 0:
        pares[e] = num[d]
        e += 1
    if num[d] > maior:
        maior = num[d]
menor = maior
for d in range(30):
    if num[d] < menor:
        menor = num[d]
media = media/30
for f in range(30):
  if num[f] >= media:
    maiormedia += 1
print('Números pares encontrados: {}'.format(pares))
print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))
print('Números maiores que a média: {}'.format(maiormedia))
