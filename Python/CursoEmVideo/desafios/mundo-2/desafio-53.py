frase = input('Escreva uma frase: ').upper().replace(" ",'')
c = len(frase)
fraseinv = (frase[c::-1])
print('{} invertido é {}.'.format(frase.strip(),fraseinv.strip()))
if fraseinv == frase:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')

