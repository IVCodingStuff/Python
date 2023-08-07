print('Insira as medidas das retas e informarei se podem ou não formar um triângulo.')
a1 = float(input('1° ângulo: '))
a2 = float(input('2° ângulo: '))
a3 = float(input('3° ângulo: '))

if (a1 + a2 > a3) and ( a2 + a3 > a1) and (a3 + a1 > a2):
    print ("Essas retas podem formar um triângulo.")
else:
    print ("Essas retas não podem formar um triângulo.")