"""Vogais na palavra"""
palavras = ('VIAJAR', 'PASSAGEM', 'AEROMOÇA', 'BAGAGEM', 'PILOTO', 'ASSENTO')
vogais = "AEIOU"
a = 0
while a < len(palavras):
    print("Na palavra {} temos".format(palavras[a], end= ''))
    for letra in palavras[a]:
        if letra in vogais:
            print(letra, end =" ")
    print()
    a += 1