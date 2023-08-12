s = int()
for c in range(0,6):
    n = int(input('Insira um número inteiro:'))
    if n % 2 == 0:
        s += n
print ('O valor da soma dos números pares inseridos é: {}'.format(s))