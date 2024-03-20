n = int(input('Quantos valores deseja em cada vetor?'))
a = [0]*n
b = [0]*n
soma = [0]*n
for c in range(n):
    a[c] = float(input('{}º valor de A: '.format(c)))
    b[c] = float(input('{}º valor de B: '.format(c)))
for d in range(n):
    soma[d] = a[d] +b[d]
    print('Soma {}: {}'.format(d, soma[d]))