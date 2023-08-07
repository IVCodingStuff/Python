print('Insira três números e direi qual o menor e o maior!')
n1 = int((input('1° número: ')))
n2 = int((input('2° número: ')))
n3 = int((input('3° número: ')))

if n1 > n2:
    maior = n1
else:
    maior = n2
    if n3 > n2:
        maior = n3
print (maior)

if n1 < n2:
    menor = n1
else:
    menor = n2
    if n3 < n2:
        menor = n3
print (menor)

    