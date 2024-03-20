"""Listagem de preços"""

precos = ['Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Compasso', 9.99,'Mochila',135.99]
print("------------------------\n   LISTAGEM DE PREÇOS\n------------------------")
a = 0
print (len(precos))
while a < len(precos) :
    print("{}................R$ {}".format(precos[a], precos[a+1]))
    a += 2

    