div = int()
n = int(input('Insira um número e descubra se ele é primo: '))
for c in range(1, n+1):
    if n % c == 0:
        div = div + 1
if div > 2:
    print ('Esse número não é primo.')
else:
    print('Esse número é primo.')