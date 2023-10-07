media = 0
maior = 0
num = [0]*5
pares =[0]*5
e = 0
for c in range(5):
    num[c] = int(input('Insira o {}º número: '.format(c+1)))
for d in range(5):    
    if num[d] % 2 == 0:
        pares[e] = num[d]
        e += 1
    if num[d] > maior:
        maior = num[d]
menor = maior
for d in range(5):
    if num[d] < menor:
        menor = num[d]

print('Números pares encontrados: {}'.format(pares))
print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))