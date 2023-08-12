maior = int()
menor = int()

for c in range (1,3):
    anonasc = int((input('Em que ano nasceu a {}º pessoa? '.format(c))))
    if anonasc < 2006:
        maior = maior + 1
    else:
        menor = menor + 1
print('Há {} pessoas maiores de idade e {} menores.'.format(maior,menor))
