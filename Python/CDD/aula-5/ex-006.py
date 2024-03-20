entre10e20 = int()
fora = int()
for c in range(1,11,1):
    num = int(input('Insira um número:'))
    if num >= 10 and num <= 20:
        entre10e20 += 1
fora = c - entre10e20
print('Número que não estão entre 10 e 20: {}'.format(fora))
print('Números entre 10 e 20: {}'.format(entre10e20))