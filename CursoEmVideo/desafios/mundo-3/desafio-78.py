# Lendo valores, dizendo onde e quais são o maior e o menor
lista = [0, 0, 0, 0, 0]
maior = 0
for a in range(0, 5):
    lista[a] = int(input('Insira um número: '))
    if maior < lista[a]:
        maior = lista[a]
        posiMaior = a
menor = maior
for b in range(5):
    if lista[b] < menor:
        menor = lista[b]
        posiMenor = b

print('O maior valor digitado foi {} na posição {}'.format(maior, posiMaior))
print('O menor valor digitado foi {} na posição {}'.format(menor, posiMenor))
